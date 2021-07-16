# Watershed를 이용한 Image Segmentation

import numpy as np
import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('./images/water_coins.jpg')
img1 = cv2.imread('./images/water_coins.jpg', 0)

_, thresh = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.subplot(2,2,1)
plt.hist(img1.ravel(), 256)
plt.title('what')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2)
plt.hist(gray.ravel(), 256)
plt.title('good')
plt.xticks([]), plt.yticks([])
plt.show()
