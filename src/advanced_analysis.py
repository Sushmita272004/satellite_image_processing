import numpy as np

# ✅ Advanced statistical analysis
def compute_advanced_stats(deformation):
    std_vals = [np.std(d) for d in deformation]

    affected_area = []
    uplift = []
    subsidence = []

    for d in deformation:
        # 🔹 Adaptive threshold (more scientific)
        threshold = np.mean(np.abs(d)) + np.std(d)

        # 🔹 Percentage of affected area
        affected = ((np.abs(d) > threshold).sum() / d.size) * 100
        affected_area.append(affected)

        # 🔹 Uplift & Subsidence percentages
        uplift.append(((d > 0).sum() / d.size) * 100)
        subsidence.append(((d < 0).sum() / d.size) * 100)

    return std_vals, affected_area, uplift, subsidence


# ✅ Hotspot detection (binary mask)
def detect_hotspots(deformation, threshold=0.05):
    hotspots = []
    for d in deformation:
        hotspots.append(np.abs(d) > threshold)
    return hotspots


# ✅ Hotspot intensity (NEW – useful for analysis)
def compute_hotspot_intensity(deformation):
    intensity = [np.mean(np.abs(d)) for d in deformation]
    return intensity