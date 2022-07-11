# 여러 개의 데이터

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

X = np.random.randint(25, 50, (25,2))
Y = np.random.randint(60, 85, (25,2))
Z = np.vstack((X,Y))

# print(X)

# np.float32로 변환 
Z = np.float32(Z)

# print(Z.shape)

# kmeans 매개변수 정의 
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center=cv.kmeans(Z, 2, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

# 데이터 분리 
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]

# 데이터 가시화
plt.scatter(A[:,0], A[:,1])
plt.scatter(B[:,0], B[:,1], c = 'r')
plt.scatter(center[:,0], center[:,1], s = 80, c = 'y', marker = 's')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()
