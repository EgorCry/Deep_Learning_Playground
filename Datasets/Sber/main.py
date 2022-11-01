from model import Model
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def change_initial_dataframe(dataframe):
    dataframe.columns = dataframe.columns.str.lower()
    dataframe['reportdate'] = dataframe['reportdate'].str.replace('.', '/')
    dataframe["reportdate"] = pd.to_datetime(dataframe["reportdate"], infer_datetime_format=True)

    return dataframe


def create_dataset(data, window):
    x = []
    y = []
    for i in range(window, data.shape[0]):
        x.append(data[i - window:i, 0])
        y.append(data[i, 0])
    x = np.array(x)
    y = np.array(y)
    return x, y


def create_dataframe(dates, values):
    nswr = pd.DataFrame({'dates': dates, 'values': values})
    return nswr


def show_plot(forecast, init_data):
    plt.figure(figsize=(14, 7))

    plt.plot(forecast['dates'], forecast['values'])
    plt.plot(init_data['reportdate'], init_data['value'])

    plt.savefig('forecast.png')


def model_forecast(init_date, window, data):
    window = int(window[:-1]) * 30

    data = data['value'].values.reshape((-1, 1))

    x_train, y_train = create_dataset(data, window)

    model = Model(window)
    model.fit(x_train, y_train)

    prediction = model.predict(data)

    dates = model.make_dates(init_date)

    forecast = create_dataframe(dates, prediction)

    return model, forecast


if __name__ == '__main__':
    df = pd.read_csv('DS_Sber.csv', sep=';')
    df = change_initial_dataframe(df)
    data = df.copy()
    
    init_date = input('Input initial date in format: YYYY-MM-DD\n')
    window = input('Input how many months do you need: 1M - 12M\n')

    init_date = np.datetime64(init_date)
    ind = data[data['reportdate'] == init_date].index
    data = data[:ind[0]]
    df = df[:ind[0]]

    model, forecast = model_forecast(init_date, window, data)

    nswr = input('Save the model? (Yes/No)\n').lower()

    if nswr == 'yes':
        model.save_model()

    show_plot(forecast, df)
