import matplotlib.pyplot as plt
import os

def plot_time_series(mean_vals, output_path):

    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    # Plot deformation trend
    plt.plot(mean_vals, marker='o', label='Mean Deformation')

    # ✅ Month labels (IMPORTANT)
    months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
    plt.xticks(range(len(mean_vals)), months[:len(mean_vals)])

    # Labels and title
    plt.title("Deformation Trend Over Time")
    plt.xlabel("Months")
    plt.ylabel("Mean Deformation")

    # Grid and legend
    plt.grid()
    plt.legend()

    # Improve layout
    plt.tight_layout()

    plt.savefig(f"{output_path}/time_series.png")
    plt.close()

# 📈 Deformation + Variability graph
def plot_deformation_and_variability(mean_vals, std_vals, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    plt.plot(mean_vals, marker='o', label='Mean Deformation')
    plt.plot(std_vals, marker='s', linestyle='--', label='Variability (Std Dev)')

    plt.title("Deformation and Variability Over Time")
    plt.xlabel("Time (Months)")
    plt.ylabel("Value")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig(f"{output_path}/deformation_variability.png")
    plt.close()


# 🌍 Affected Area graph
def plot_affected_area(affected_area, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    plt.plot(affected_area, marker='o')
    plt.title("Affected Area Percentage Over Time")
    plt.xlabel("Time (Months)")
    plt.ylabel("Affected Area (%)")
    plt.grid()

    plt.tight_layout()
    plt.savefig(f"{output_path}/affected_area.png")
    plt.close()


# ⬆️⬇️ Uplift vs Subsidence graph
def plot_uplift_subsidence(uplift, subsidence, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    plt.plot(uplift, marker='o', label='Uplift (%)')
    plt.plot(subsidence, marker='s', label='Subsidence (%)')

    plt.title("Uplift vs Subsidence Over Time")
    plt.xlabel("Time (Months)")
    plt.ylabel("Percentage (%)")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig(f"{output_path}/uplift_subsidence.png")
    plt.close()

def plot_future_prediction(mean_vals, future_predictions, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    # Past data
    x_past = list(range(len(mean_vals)))
    plt.plot(x_past, mean_vals, marker='o', label='Observed')

    # Future data
    x_future = list(range(len(mean_vals), len(mean_vals) + len(future_predictions)))
    plt.plot(x_future, future_predictions, marker='x', linestyle='--', label='Predicted')

    # Month labels
    months = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
    future_labels = [f'+{i+1}' for i in range(len(future_predictions))]
    all_labels = months + future_labels

    plt.xticks(range(len(all_labels)), all_labels)

    plt.title("Deformation Trend with Future Prediction")
    plt.xlabel("Time (Months + Future)")
    plt.ylabel("Mean Deformation")

    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig(f"{output_path}/future_prediction.png")
    plt.close()