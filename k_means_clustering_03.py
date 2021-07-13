# 색상 양자화
import numpy as np
import cv2

img = cv2.imread('./images/clustering.jpg')
img = cv2.resize(img, (480, 480))
z = img.reshape((-1, 3))

z = np.float32(z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k3 = 3 
k6 = 6
k9 = 9
ret3, label3, center3 = cv2.kmeans(z, k3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
ret6, label6, center6 = cv2.kmeans(z, k6, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
ret9, label9, center9 = cv2.kmeans(z, k9, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)


center3 = np.uint8(center3)
res3 = center3[label3.flatten()]
res3 = res3.reshape(img.shape)

center6 = np.uint8(center6)
res6 = center6[label6.flatten()]
res6 = res6.reshape(img.shape)

center9 = np.uint8(center9)
res9 = center9[label9.flatten()]
res9 = res9.reshape(img.shape)

cv2.imshow('Original', img)
cv2.imshow('K = 3', res3)
cv2.imshow('K = 6', res6)
cv2.imshow('K = 9', res9)

cv2.waitKey(0)
cv2.destroyAllWindows()