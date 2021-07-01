import cv2

image = cv2.imread('mnist.png', cv2.IMREAD_GRAYSCALE)

for m, i in enumerate(range(0, image.shape[0], 20)):
    for j in range(0, image.shape[1], 20):
        img = image[i:i+20, j:j+20]
        g = m//5
        cv2.imwrite(f'Mnist/{g}/{i}{j}.jpg', img)