<<<<<<< HEAD
# grayscale을 만드는 imread와 cvtColor를 비교해보고 실제로 픽셀에 차이가 있는지 확인해보기 

=======
>>>>>>> 914c77c969ffda921461299951962fc7a4f91d2c
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/lena.jpg')

gray1 = cv2.imread('./images/lena.jpg', 0)
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

diff = cv2.subtract(gray1, gray2)

_, th = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

images = [gray1, gray2, th]

titles = ['imread_gray',
          'cvtColor_gray',
          'sub_threshold']

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap = 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()