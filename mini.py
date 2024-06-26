# -*- coding: utf-8 -*-
"""MINIIII.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g4fRztgiaBZIZFMRND68G4DppX76oGiH
"""

import pandas as pd

data=pd.read_csv("/content/REVIEW2.csv")

y=data.iloc[:,8]
x=data.iloc[:,0:8]

# Splitting the dataset into training and test set.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)
k=knn.fit(x_train, y_train)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

rf_classifier.fit(x_train, y_train)
y_pred = rf_classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_train, y_train)

# Save the trained model
joblib.dump(rf_classifier, 'random_forest_model.pkl')

def get_user_input():
    features = ['snoring range', 'respiration rate', 'body temperature', 'limb movement rate',
                'blood oxygen levels', 'eye movement', 'number of hours of sleep', 'heart rate']
    user_input = []
    for feature in features:
        value = float(input(f"Enter {feature}: "))
        user_input.append(value)
    return user_input

def preprocess_input(user_input):
    scaler = StandardScaler()
    user_input = np.array(user_input).reshape(1, -1)
    scaled_input = scaler.fit_transform(user_input)
    return scaled_input

def predict(user_input):
    # Load the trained model
    rf_classifier = joblib.load('random_forest_model.pkl')
    prediction = rf_classifier.predict(user_input)
    return prediction

def display_results(prediction):
    stress_levels_mapping = {
        0: 'low/normal',
        1: 'medium low',
        2: 'medium',
        3: 'medium high',
        4: 'high'
    }
    predicted_stress_level = stress_levels_mapping[int(prediction)]
    percentage_range = (int(prediction) * 25, (int(prediction) + 1) * 25 - 1)
    qualitative_description = {
        0: 'low',
        1: 'medium',
        2: 'medium',
        3: 'medium',
        4: 'high'
    }
    print(f"Predicted Stress Level: {predicted_stress_level} ({percentage_range[0]}% to {percentage_range[1]}%, {qualitative_description[int(prediction)]})")

def main():
    user_input = get_user_input()
    preprocessed_input = preprocess_input(user_input)
    prediction = predict(preprocessed_input)
    display_results(prediction)

if __name__ == "__main__":
    main()