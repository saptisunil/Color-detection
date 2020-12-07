import numpy as np
import cv2

image = cv2.imread('BLUE_INPUT.jpg')
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([94,80,2])
upper = np.array([126,255,255])
mask = cv2.inRange(image, lower, upper)
result = cv2.bitwise_and(result, result, mask=mask)

cv2.imshow('result', result)
cv2.waitKey()
