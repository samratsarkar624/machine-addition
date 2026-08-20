import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Training examples
# The model is given examples, NOT the addition rule.

X = np.array([
    [1, 2],
    [2, 7],
    [4, 3],
    [5, 8],
    [9, 1],
    [6, 4],
    [3, 8],
    [7, 5],
    [10, 2],
    [4, 9],
    [12, 3],
    [8, 6],
    [15, 4],
    [11, 7],
    [2, 13]
])

y = np.array([
    3,
    9,
    7,
    13,
    10,
    10,
    11,
    12,
    12,
    13,
    15,
    14,
    19,
    18,
    15
])

# Create ML model
model = LinearRegression()

# Train model
model.fit(X, y)

# Save trained model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")
