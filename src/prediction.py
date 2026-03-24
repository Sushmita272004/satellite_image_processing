import numpy as np
from sklearn.linear_model import LinearRegression

def predict_future_risk(mean_vals):
    X = np.arange(len(mean_vals)).reshape(-1, 1)
    y = np.array(mean_vals)

    model = LinearRegression()
    model.fit(X, y)

    future_months = np.arange(len(mean_vals), len(mean_vals)+6).reshape(-1, 1)
    predictions = model.predict(future_months)

    return predictions

def calculate_risk(predictions):
    risk_levels = []

    for val in predictions:
        if val > 0.7:
            risk_levels.append("HIGH")
        elif val > 0.4:
            risk_levels.append("MEDIUM")
        else:
            risk_levels.append("LOW")

    return risk_levels