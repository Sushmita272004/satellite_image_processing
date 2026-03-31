import matplotlib.pyplot as plt
import numpy as np
import os


# ✅ Deformation map plotting
def plot_deformation_maps(deformation, output_path):
    os.makedirs(output_path, exist_ok=True)

    for i, diff in enumerate(deformation):
        plt.figure()

        im = plt.imshow(diff, cmap='seismic', vmin=-0.01, vmax=0.01)
        plt.colorbar(im, label='Deformation')

        plt.title(f'Month {i+1} → {i+2}')
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")

        plt.tight_layout()  # ✅ prevents cut labels
        plt.savefig(f"{output_path}/deformation_{i+1}.png")
        plt.close()


# ✅ Basic statistics
def compute_statistics(deformation):
    mean_vals = [np.mean(d) for d in deformation]
    max_vals = [np.max(d) for d in deformation]
    min_vals = [np.min(d) for d in deformation]

    return mean_vals, max_vals, min_vals


# ✅ Hotspot visualization
def plot_hotspots(hotspots, output_path):
    os.makedirs(output_path, exist_ok=True)

    for i, h in enumerate(hotspots):
        plt.figure()

        im = plt.imshow(h, cmap='gray')
        plt.colorbar(im, label='Hotspot Presence')

        plt.title(f"Hotspots Month {i+1}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")

        plt.tight_layout()
        plt.savefig(f"{output_path}/hotspot_{i+1}.png")
        plt.close()