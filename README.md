# 🌍 Land Deformation Analysis using Satellite Images

## 📌 Overview

This project analyzes **land deformation over time** using multi-temporal satellite `.tiff` images. It computes deformation between consecutive months, performs statistical and spatial analysis, and predicts future deformation trends.

---

## 🎯 Objectives

- Analyze **temporal land deformation patterns**
- Identify **unstable regions (hotspots)**
- Quantify **uplift and subsidence behavior**
- Study **deformation variability and affected area**
- Predict **future deformation trends and risk levels**

---

## 📂 Project Structure

```
land_deformation_project/
├── data/                         # Input satellite TIFF images
├── output/
│ ├── maps/                       # Deformation maps & graphs
│ ├── plots/                      # Additional visualizations
│ └── results.csv                 # Statistical results
├── src/
│ ├── load_data.py                # Data loading
│ ├── preprocess.py               # Normalization & smoothing
│ ├── analysis.py                 # Visualization & statistics
│ ├── prediction.py               # Future prediction model
│ ├── visualization.py            # Graph plotting
│ ├── anomaly.py                  # Anomaly detection
│ ├── advanced_analysis.py        # Advanced metrics
│ └── main.py                     # Main pipeline
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
pip install numpy rasterio matplotlib pandas scikit-learn scipy

```

## ▶️ Run the Project

```
python src/main.py
```

---

## 🔬 Methodology

```
1. Data Loading
 -Multi-temporal satellite .tiff images are loaded

2. Preprocessing
 -Normalization
 -Gaussian smoothing (noise reduction)

3. Deformation Computation
 -Month-to-month difference:
    Deformation = Image(t) - Image(t-1)

4. Spatial Analysis
 -Deformation maps (heatmaps)
 -Hotspot detection

5. Statistical Analysis
 -Mean, Max, Min deformation
 -Standard deviation (variability)
 -Affected area percentage
 -Uplift vs Subsidence ratio

6. Temporal Analysis
 -Time series visualization
 -Trend and variability analysis

7. Prediction
 -Polynomial regression for future deformation
 -Risk classification (Low / Medium / High)

8. Anomaly Detection
 -Z-score based detection on combined signals

```

## 📊 Results & Observations
 -Mean deformation values are generally small → overall regional stability
 -Spatial maps reveal localized deformation zones
 -Increasing variability over time indicates growing instability
 -Shift from uplift to subsidence suggests potential ground weakening
 -Affected area increases gradually, showing spatial spread of deformation


## 📈 Key Visual Outputs
 -Deformation Maps (Month-to-Month)
 -Time Series Trend
 -Deformation vs Variability Graph
 -Affected Area Analysis
 -Uplift vs Subsidence Comparison
 -Future Prediction Graph

## ⚠️ Key Insight

Even when average deformation is small, localized hotspots indicate real risk zones.
Spatial analysis is crucial for accurate interpretation.

## 🔍 Model Interpretation
 -The model does not rely on prior event knowledge
 -It detects behavioral changes in land deformation
 -Transition zones indicate emerging instability patterns

## 🔮 Conclusion

 -The region appears globally stable, but shows localized deformation and increasing variability over time.
 -This highlights the importance of continuous monitoring for early warning of land instability.

## 🚀 Future Improvements
 -Integration with InSAR phase-based analysis
 -Deep learning models (LSTM / Time-series forecasting)
 -GIS-based visualization
 -Real-time monitoring system
 -Multi-region comparative analysis