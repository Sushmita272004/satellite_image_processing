from load_data import load_tiff_images
from preprocess import normalize_images, compute_deformation, smooth_images
from analysis import plot_deformation_maps, compute_statistics
from prediction import predict_future_risk, calculate_risk
from advanced_analysis import compute_advanced_stats, detect_hotspots
from visualization import plot_time_series
from anomaly import detect_anomalies

import os
import pandas as pd
import numpy as np

# ✅ Define paths FIRST
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data")
OUTPUT_MAP_PATH = os.path.join(BASE_DIR, "output", "maps")
OUTPUT_CSV_PATH = os.path.join(BASE_DIR, "output", "results.csv")

# ✅ Debug check
print("DATA PATH:", DATA_PATH)
print("FILES:", os.listdir(DATA_PATH))

# 1. Load data
images, filenames = load_tiff_images(DATA_PATH)

# 2. Normalize + Smooth
images = normalize_images(images)
images = smooth_images(images)

# 3. Compute deformation
deformation = compute_deformation(images)

# 4. Plot maps
plot_deformation_maps(deformation, OUTPUT_MAP_PATH)

# 5. BASIC Statistics (⚠️ YOU MISSED THIS)
mean_vals, max_vals, min_vals = compute_statistics(deformation)

# 6. ADVANCED Statistics
std_vals, affected_area, uplift, subsidence = compute_advanced_stats(deformation)

# 7. Time series
plot_time_series(mean_vals, OUTPUT_MAP_PATH)

# 8. Prediction
future_predictions = predict_future_risk(mean_vals)
risk_levels = calculate_risk(future_predictions)

# 9. Hotspots
hotspots = detect_hotspots(deformation)

# 10. Anomaly Detection (Improved)
combined_signal = np.array(mean_vals) + np.array(std_vals)
z_scores, anomalies = detect_anomalies(combined_signal)

print("Z-Scores:", z_scores)
print("Anomalies:", anomalies)

# 11. Save results
df = pd.DataFrame({
    "Month": filenames[1:],
    "Mean": mean_vals,
    "Std": std_vals,
    "Max": max_vals,
    "Min": min_vals,
    "Affected Area %": affected_area,
    "Uplift %": uplift,
    "Subsidence %": subsidence
})

df.to_csv(OUTPUT_CSV_PATH, index=False)

# 12. Mining Impact Analysis (MOST IMPORTANT)
before = mean_vals[:4]   # before July
after = mean_vals[4:]    # after July

print("---- Mining Impact Analysis ----")
print("Before Avg:", np.mean(before))
print("After Avg:", np.mean(after))
print("Change:", np.mean(after) - np.mean(before))

# Final outputs
print("Future Predictions:", future_predictions)
print("Risk Levels:", risk_levels)