from load_data import load_tiff_images
from preprocess import normalize_images, compute_deformation
from analysis import plot_deformation_maps, compute_statistics
from prediction import predict_future_risk, calculate_risk

import os
import pandas as pd

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

# 2. Normalize
images = normalize_images(images)

# 3. Compute deformation
deformation = compute_deformation(images)

# 4. Plot maps
plot_deformation_maps(deformation, OUTPUT_MAP_PATH)

# 5. Statistics
mean_vals, max_vals, min_vals = compute_statistics(deformation)

# 6. Prediction
future_predictions = predict_future_risk(mean_vals)
risk_levels = calculate_risk(future_predictions)

# 7. Save results
df = pd.DataFrame({
    "Month": filenames[1:],
    "Mean": mean_vals,
    "Max": max_vals,
    "Min": min_vals
})

df.to_csv(OUTPUT_CSV_PATH, index=False)

print("Future Predictions:", future_predictions)
print("Risk Levels:", risk_levels)