import joblib

model = joblib.load("model.pkl")


def predict(a, b):
    prediction = model.predict([[a, b]])
    return prediction[0]