import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression


class Model:
    def __init__(self, window):
        self.model = LinearRegression()
        self.window = window

    def fit(self, x, y):
        self.model.fit(x, y)

    def score_model(self, x, y):
        return self.model.score(x, y)

    def intercept_model(self):
        return self.model.intercept_

    def coef_model(self):
        return self.model.coef_

    def predict(self, data):
        nswr = data.copy()

        for _ in range(self.window):
            x_data = nswr[-self.window:].reshape(1, self.window)

            prediction = self.model.predict(x_data)
            
            nswr = np.append(nswr, prediction)

        return nswr[-self.window:]

    def save_model(self):
        filename = 'sber_model.sav'
        pickle.dump(self.model, open(filename, 'wb'))

    def make_dates(self, init_date):
        date = init_date

        dates = np.array([]).astype('datetime64')

        for _ in range(self.window):
            date += np.timedelta64(1, 'D')

            dates = np.append(dates, date)

        return dates
