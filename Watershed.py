# Watershed를 이용한 Image Segmentation

import numpy as np
import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('./images/water_coins.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

cv2.imshow("thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()