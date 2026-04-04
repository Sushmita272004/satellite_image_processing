import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def predict_future_risk(mean_vals):
    X = np.arange(len(mean_vals)).reshape(-1, 1)
    y = np.array(mean_vals)

    # Polynomial transformation (degree = 2)
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    # Future months
    future_months = np.arange(len(mean_vals), len(mean_vals)+6).reshape(-1, 1)
    future_poly = poly.transform(future_months)

    predictions = model.predict(future_poly)

    return predictions

def calculate_risk(predictions):
    risk_levels = []

    mean = np.mean(predictions)
    std = np.std(predictions)

    for val in predictions:
        if val > mean + std:
            risk_levels.append("HIGH")
        elif val > mean:
            risk_levels.append("MEDIUM")
        else:
            risk_levels.append("LOW")

    return risk_levels

