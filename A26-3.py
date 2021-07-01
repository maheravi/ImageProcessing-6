import cv2
import numpy as np

image = cv2.imread('board.tif', cv2.IMREAD_GRAYSCALE)

kernel2 = np.ones((7, 7), dtype=float) / 49

result2 = cv2.filter2D(image, -1, kernel2)

cv2.imshow('output', result2)
cv2.imwrite('board_out.tif', result2)
cv2.waitKey()
