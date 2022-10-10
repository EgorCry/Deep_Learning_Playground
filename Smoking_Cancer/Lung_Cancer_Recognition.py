import tensorflow as tf
import numpy as np
from pickle import load


def model_predict():
    model = tf.keras.models.load_model('saved_model/lung_cancer_model')
    scaler = load(open('scaler.pkl', 'rb'))

    age = input('Please enter age from 21 to 87\n')
    smoking = 1 if input('Please enter if you smoking (yes or no)\n').lower() == 'yes' else 0
    yellow_fingers = 1 if input('Please enter if you have yellow fingers (yes or no)\n').lower() == 'yes' else 0
    anxiety = 1 if input('Please enter if you have anxiety (yes or no)\n').lower() == 'yes' else 0
    peer_pressure = 1 if input('Please enter if you have pressure from your peers (yes or no)\n').lower() == 'yes' else 0
    chronic_disease = 1 if input('Please enter if you have any chronic disease (yes or no)\n').lower() == 'yes' else 0
    fatigue = 1 if input('Please enter if you have fatigue (yes or no)\n').lower() == 'yes' else 0
    allergy = 1 if input('Please enter if you have allergy (yes or no)\n').lower() == 'yes' else 0
    wheezing = 1 if input('Please enter if you have wheezing (yes or no)\n').lower() == 'yes' else 0
    alcohol_consuming = 1 if input('Please enter if you drinking alcohol (yes or no)\n').lower() == 'yes' else 0
    coughing = 1 if input('Please enter if you coughing (yes or no)\n').lower() == 'yes' else 0
    shortness_of_breath = 1 if input('Please enter if you have difficulties with breathing (yes or no)\n').lower() == 'yes' else 0
    swallowing_difficulty = 1 if input('Please enter if you swallowing with difficulties (yes or no)\n').lower() == 'yes' else 0
    chest_pain = 1 if input('Please enter if you have chest pain (yes or no)\n').lower() == 'yes' else 0

    rqst = np.array([age, smoking, yellow_fingers, anxiety, peer_pressure,
                      chronic_disease, fatigue, allergy, wheezing, alcohol_consuming,
                      coughing, shortness_of_breath, swallowing_difficulty, chest_pain])

    rqst_scaled = tf.reshape(rqst, [-1, 14])

    rqst_scaled = scaler.transform(rqst_scaled)

    result = model.predict(rqst_scaled)
    result_scaled = 1 if result >= 0.5 else 0
    result = round(result[0][0] * 100, 2)

    if result_scaled == 1:
        print(f'You have lung cancer with {result}% sure.')
    else:
        print(f"You don't have cancer with {100-result}% sure")


if __name__=='__main__':
    model_predict()
