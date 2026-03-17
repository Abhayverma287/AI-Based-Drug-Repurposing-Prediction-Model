import joblib
import numpy as np

# Load model
model = joblib.load("models/repurposing_model.pkl")

def predict_disease(f1, f2, f3, f4):

    features = np.array([[f1, f2, f3, f4]])

    prediction = model.predict(features)

    return prediction[0]