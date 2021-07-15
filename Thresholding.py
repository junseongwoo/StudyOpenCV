# Thresholding (스레시홀딩)

import cv2
import numpy as np 
from matplotlib import pyplot as plt

## Global Thresholding
# img = cv2.imread('./images/gradient.png', 0)
# _, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# _, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# _, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# _, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# _, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# for i in range(6):
#     plt.subplot(2, 3, i+1)
#     plt.imshow(images[i], 'gray', vmin = 0, vmax = 255)
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# plt.show()

## Adaptive Thresholding
img = cv2.imread('./images/sudoku.png', 0)
img = cv2.medianBlur(img, 5)

_, thresh1 = cv2.threshold(img, 127 , 255, cv2.THRESH_BINARY)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

titles = ['Original Image', 'Global Threshoding ( v = 127 )', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, thresh1, thresh2, thresh3]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()



