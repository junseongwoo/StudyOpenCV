# 오츠 이진화 

import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/noise_img.png', 0)

# 전역 스레시홀딩
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 오츠 스레시홀딩
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_OTSU)

# 가우시안 필터 후 오츠 스레시홀딩 
blur = cv2.GaussianBlur(img, (5,5), 0 )
_, th3 = cv2.threshold(blur, 127, 255, cv2.THRESH_OTSU)

# 이미지 및 이미지의 히스토그램 출력 
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Nosie Image', 'Histogram', 'Global Thresholding ( v = 127 )',
          'Original Nosie Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian Image', 'Histogram', "Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3, 3, i*3+1)
    plt.imshow(images[i*3], cmap = 'gray')
    plt.title(titles[i*3])
    plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i*3+2) 
    plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1])
    plt.xticks([]), plt.yticks([])

    plt.subplot(3, 3, i*3+3) 
    plt.imshow(images[i*3+2], cmap = 'gray')
    plt.title(titles[i*3+2])
    plt.xticks([]), plt.yticks([])
    
plt.show()
