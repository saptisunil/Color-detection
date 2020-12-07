import numpy as np
import cv2

image = cv2.imread('PARROT_INPUT.jpg')
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([25,52,72])
upper = np.array([102,255,255])
mask = cv2.inRange(image, lower, upper)
result = cv2.bitwise_and(result, result, mask=mask)

cv2.imshow('result', result)
cv2.waitKey()

