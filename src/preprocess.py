import numpy as np
from scipy.ndimage import gaussian_filter


# ✅ Smooth images to reduce noise
def smooth_images(images):
    smoothed = []
    for img in images:
        smoothed.append(gaussian_filter(img, sigma=1))
    return np.array(smoothed)


# ✅ Normalize images (safe version)
def normalize_images(images):
    norm_images = []

    for img in images:
        min_val = np.min(img)
        max_val = np.max(img)

        # ✅ Prevent division by zero
        if max_val - min_val == 0:
            norm_images.append(img)
        else:
            norm_img = (img - min_val) / (max_val - min_val)
            norm_images.append(norm_img)

    return np.array(norm_images)


# ✅ Compute deformation (temporal difference)
def compute_deformation(images):
    deformation = []

    for i in range(1, len(images)):
        diff = images[i] - images[i - 1]

        # ✅ Smooth deformation (reduces noise)
        diff = gaussian_filter(diff, sigma=1)

        # ✅ Normalize deformation scale (optional but useful)
        max_abs = np.max(np.abs(diff))
        if max_abs != 0:
            diff = diff / max_abs

        deformation.append(diff)

    return np.array(deformation)