import matplotlib.pyplot as plt
import numpy as np
import os

def plot_deformation_maps(deformation, output_path):
    os.makedirs(output_path, exist_ok=True)

    for i, diff in enumerate(deformation):
        plt.imshow(diff, cmap='seismic', vmin=-0.01, vmax=0.01)
        plt.colorbar(label='Deformation')
        plt.title(f'Month {i+1} → {i+2}')
        plt.savefig(f"{output_path}/deformation_{i+1}.png")
        plt.close()

def compute_statistics(deformation):
    mean_vals = [np.mean(d) for d in deformation]
    max_vals = [np.max(d) for d in deformation]
    min_vals = [np.min(d) for d in deformation]

    return mean_vals, max_vals, min_vals