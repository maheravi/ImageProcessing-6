import cv2
import os

image = cv2.imread('mnist.png', cv2.IMREAD_GRAYSCALE)

for m, i in enumerate(range(0, image.shape[0], 20)):
    g = m // 5
    parent_dir = "Mnist"
    directory = (f'{g}')
    path = os.path.join(parent_dir, directory)
    try:
        os.makedirs(path, exist_ok=True)
        print("Directory '%s' created successfully" % directory)
    except OSError as error:
        print("Directory '%s' can not be created" % directory)

    for j in range(0, image.shape[1], 20):
        img = image[i:i+20, j:j+20]
        cv2.imwrite(f'Mnist/{g}/{i}{j}.jpg', img)
