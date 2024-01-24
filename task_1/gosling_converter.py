import cv2
import numpy as np

def threshold_image(image_path, value):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    my_image = np.zeros_like(image)

    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            if image[i, j] > value:
                my_image[i, j] = 228

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("/usr/app/src/result.jpg", my_image)

image_path = "/usr/app/src/gosl.jpg"
value = 42

threshold_image(image_path, value)


import os

target_folder = 'C:/docker_ssau/Artificial-Intelligence-Lab-2/task_1/data'

os.makedirs(target_folder, exist_ok=True)

import shutil

source_path = '/usr/app/src/result.jpg'

target_path = 'C:/docker_ssau/Artificial-Intelligence-Lab-2/task_1/result.jpg'

shutil.copy(source_path, target_path)

