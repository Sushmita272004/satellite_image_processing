import matplotlib.pyplot as plt
import os

def plot_time_series(mean_vals, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    # Plot deformation trend
    plt.plot(mean_vals, marker='o', label='Mean Deformation')

    # ✅ Highlight mining event (July index = 4 approx)
    plt.axvline(x=3.5, linestyle='--', label='Mining Event (July)')

    # Labels and title
    plt.title("Deformation Trend Over Time")
    plt.xlabel("Time (Months)")
    plt.ylabel("Mean Deformation")

    # Grid and legend
    plt.grid()
    plt.legend()

    # Improve layout
    plt.tight_layout()

    plt.savefig(f"{output_path}/time_series.png")
    plt.close()