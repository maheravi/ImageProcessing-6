import cv2

image = cv2.imread('flower_input.jpg', cv2.IMREAD_GRAYSCALE)

result = cv2.blur(image, (7, 7))

for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if image[i, j] > 125:
            result[i, j] = image[i, j]

cv2.imshow('output', result)
cv2.waitKey()

