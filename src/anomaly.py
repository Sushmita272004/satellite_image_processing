import numpy as np

def detect_anomalies(mean_vals):
    mean = np.mean(mean_vals)
    std = np.std(mean_vals)

    # ✅ Avoid division by zero
    if std == 0:
        z_scores = [0 for _ in mean_vals]
        anomalies = [False for _ in mean_vals]
        return z_scores, anomalies

    # ✅ Z-score calculation
    z_scores = [(val - mean) / std for val in mean_vals]

    # ✅ Detect anomalies
    anomalies = [abs(z) > 2 for z in z_scores]

    return z_scores, anomalies