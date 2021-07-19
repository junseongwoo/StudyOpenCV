# Watershed를 이용한 Image Segmentation

import numpy as np
import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('./images/water_coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 노이즈를 모폴로지 열림으로 제거 
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

# 확실한 배경 영역 찾음
sure_bg = cv2.dilate(opening, kernel, iterations = 3)

# 확실한 전경(객체) 영역 찾음
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

# 배경과 전경을 제외한 영역 찾음 
unknown = cv2.subtract(sure_bg, sure_fg)

# markers 라벨링
ret, markers = cv2.connectedComponents(sure_fg)

# 모든 라벨에 1을 더하여 배경이 0이 아니라 1이 되도록 함 
# -> unknown 지역과 같은 값을 가지는 것을 피하기 위해 
markers = markers + 1 

# unknown 지역을 0으로 마크한다.
markers[unknown == 255] = 0



plt.subplot(121)
plt.imshow(markers, cmap='jet')
plt.title('marker_jet')
plt.yticks([]), plt.xticks([])

markers = cv2.watershed(img, markers)

img[markers == -1] = [255, 0, 0]

plt.subplot(122)
plt.imshow(img)
plt.title('Watershed')
plt.yticks([]), plt.xticks([])
plt.show()