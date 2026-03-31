# 🌍 Land Deformation Analysis using Satellite Images

## 📌 Overview

This project analyzes **land deformation over time** using monthly satellite `.tiff` images. It computes deformation between consecutive months, visualizes spatial changes, and predicts future risk.

---

## 🎯 Objectives

* Analyze monthly deformation
* Detect unstable regions (hotspots)
* Study deformation trends
* Predict future risk of calamity

---

## 📂 Project Structure

```
land_deformation_project/
├── data/           # Input TIFF images
├── output/         # Maps & results
        ├──maps/
        ├──plots/   
        ├──results.csv    
├── src/   
        ├──load_data.py     # Source code
        ├──preprocess.py
        ├──analysis.py
        ├──prediction.py
        ├──main.py  
├──requirements.txt    
└── README.md
```

---

## ⚙️ Installation

```
pip install numpy rasterio matplotlib pandas scikit-learn
```

---

## ▶️ Run the Project

```
python src/main.py
```

---

## 🔬 Method

* Load satellite images
* Normalize data
* Compute deformation (month-to-month difference)
* Visualize using heatmaps
* Predict future trends using linear regression

---

## 📊 Results

* Deformation values are mostly small → **overall stable region**
* Localized red/blue regions indicate **uplift & subsidence**
* Alternating patterns show **ground instability cycles**

---

## ⚠️ Key Insight

> Mean values may appear low, but **spatial hotspots reveal real risk zones**.

---

## 💥 Validation

Deformation patterns align with a **July 2019 mining calamity**, showing the model can capture real-world events.

---

## 🔮 Conclusion

The region is generally stable, but **localized deformation exists**, highlighting the importance of continuous monitoring for early warning.

---

## 🚀 Future Work

* Deep learning (LSTM)
* GIS mapping
* Real-time monitoring

---
