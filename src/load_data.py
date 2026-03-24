import rasterio
import numpy as np
import os

def load_tiff_images(data_path):
    images = []
    filenames = sorted(os.listdir(data_path), key=lambda x: x.split('-')[1])

    for file in filenames:
        if file.endswith(".tif") or file.endswith(".tiff"):
            path = os.path.join(data_path, file)
            with rasterio.open(path) as src:
                img = src.read(1)
                images.append(img)

    return np.array(images), filenames