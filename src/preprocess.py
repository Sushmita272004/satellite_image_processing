import numpy as np

def normalize_images(images):
    norm_images = []
    for img in images:
        img = (img - np.min(img)) / (np.max(img) - np.min(img))
        norm_images.append(img)
    return np.array(norm_images)

def compute_deformation(images):
    # difference between consecutive months
    deformation = []
    for i in range(1, len(images)):
        diff = images[i] - images[i-1]
        deformation.append(diff)
    return np.array(deformation)