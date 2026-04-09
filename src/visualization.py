import matplotlib.pyplot as plt
import os

def plot_time_series(mean_vals, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    plt.plot(mean_vals, marker='o', label='Mean Deformation')

    # ✅ Interval labels
    months = ['Mar-Apr', 'Apr-May', 'May-Jun', 'Jun-Jul', 'Jul-Aug', 'Aug-Sep', 'Sep-Oct']
    plt.xticks(range(len(mean_vals)), months[:len(mean_vals)])

    plt.title("Deformation Trend Over Time")
    plt.xlabel("Time Intervals")
    plt.ylabel("Mean Deformation")

    plt.grid()
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"{output_path}/time_series.png")
    plt.close()

def plot_deformation_and_variability(mean_vals, std_vals, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    plt.plot(mean_vals, marker='o', label='Mean Deformation')
    plt.plot(std_vals, marker='s', linestyle='--', label='Variability (Std Dev)')

    months = ['Mar-Apr', 'Apr-May', 'May-Jun', 'Jun-Jul', 'Jul-Aug', 'Aug-Sep', 'Sep-Oct']
    plt.xticks(range(len(mean_vals)), months[:len(mean_vals)])

    plt.title("Deformation and Variability Over Time")
    plt.xlabel("Time Intervals")
    plt.ylabel("Value")

    plt.legend()
    plt.grid()
    plt.tight_layout()

    plt.savefig(f"{output_path}/deformation_variability.png")
    plt.close()


def plot_affected_area(affected_area, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    plt.plot(affected_area, marker='o')

    months = ['Mar-Apr', 'Apr-May', 'May-Jun', 'Jun-Jul', 'Jul-Aug', 'Aug-Sep', 'Sep-Oct']
    plt.xticks(range(len(affected_area)), months[:len(affected_area)])

    plt.title("Affected Area Percentage Over Time")
    plt.xlabel("Time Intervals")
    plt.ylabel("Affected Area (%)")

    plt.grid()
    plt.tight_layout()

    plt.savefig(f"{output_path}/affected_area.png")
    plt.close()


def plot_uplift_subsidence(uplift, subsidence, output_path):
    os.makedirs(output_path, exist_ok=True)

    plt.figure()

    plt.plot(uplift, marker='o', label='Uplift (%)')
    plt.plot(subsidence, marker='s', label='Subsidence (%)')

    months = ['Mar-Apr', 'Apr-May', 'May-Jun', 'Jun-Jul', 'Jul-Aug', 'Aug-Sep', 'Sep-Oct']
    plt.xticks(range(len(uplift)), months[:len(uplift)])

    plt.title("Uplift vs Subsidence Over Time")
    plt.xlabel("Time Intervals")
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
    months = ['Mar-Apr', 'Apr-May', 'May-Jun', 'Jun-Jul', 'Jul-Aug', 'Aug-Sep', 'Sep-Oct']
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