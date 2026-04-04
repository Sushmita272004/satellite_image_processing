from load_data import load_tiff_images
from preprocess import normalize_images, compute_deformation, smooth_images
from analysis import plot_deformation_maps, compute_statistics
from prediction import predict_future_risk, calculate_risk
from advanced_analysis import compute_advanced_stats, detect_hotspots
from visualization import plot_time_series
from anomaly import detect_anomalies
from visualization import plot_deformation_and_variability, plot_affected_area, plot_uplift_subsidence,plot_future_prediction
import os
import pandas as pd
import numpy as np

# Define paths FIRST
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data")
OUTPUT_MAP_PATH = os.path.join(BASE_DIR, "output", "maps")
OUTPUT_CSV_PATH = os.path.join(BASE_DIR, "output", "results.csv")

# Debug check
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

# 5. BASIC Statistic
mean_vals, max_vals, min_vals = compute_statistics(deformation)

# 6. ADVANCED Statistics
std_vals, affected_area, uplift, subsidence = compute_advanced_stats(deformation)
plot_deformation_and_variability(mean_vals, std_vals, OUTPUT_MAP_PATH)
plot_affected_area(affected_area, OUTPUT_MAP_PATH)
plot_uplift_subsidence(uplift, subsidence, OUTPUT_MAP_PATH)

# 7. Time series
plot_time_series(mean_vals, OUTPUT_MAP_PATH)

# 8. Prediction
future_predictions = predict_future_risk(mean_vals)
risk_levels = calculate_risk(future_predictions)

plot_future_prediction(mean_vals, future_predictions, OUTPUT_MAP_PATH)

# 9. Hotspots
hotspots = detect_hotspots(deformation)

# 10. Anomaly Detection (Improved)
combined_signal = np.array(mean_vals) + np.array(std_vals)
z_scores, anomalies = detect_anomalies(combined_signal)

print("Z-Scores:", z_scores)
print("Anomalies:", anomalies)

print("\n===== LAND DEFORMATION ANALYSIS REPORT =====\n")

# Dataset timeline
print("📁 Dataset Timeline:")
print("March → April → May → June → July → August → September → October\n")

# Z-scores (cleaned)
print("📊 Z-Scores:")
print([round(float(z), 3) for z in z_scores])

# Anomaly detection
print("\n🚨 Anomaly Detection:")
if any(anomalies):
    print("Anomalies detected at indices:", [i+1 for i, a in enumerate(anomalies) if a])
else:
    print("No significant anomalies detected")

before = mean_vals[:4]
after = mean_vals[4:]

# Deformation summary
print("\n📊 Deformation Summary:")
print(f"Before Avg: {np.mean(before):.6f}")
print(f"After Avg:  {np.mean(after):.6f}")
print(f"Net Change: {(np.mean(after) - np.mean(before)):.6f}")

# Future predictions (clean format)
print("\n📉 Future Deformation Predictions:")
for i, val in enumerate(future_predictions):
    print(f"Month +{i+1}: {float(val):.6f}")

# Risk levels (clean)
print("\n🚨 Risk Levels:")
print(" → ".join(risk_levels))

print("\n===== END OF REPORT =====\n")

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

