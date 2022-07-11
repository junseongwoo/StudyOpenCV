# 하나의 데이터 

import numpy as np
import cv2
import matplotlib.pyplot as plt

x = np.random.randint(25,100,25) 
y = np.random.randint(175,255,25)

z = np.hstack((x,y))
z = z.reshape((50,1))
z = np.float32(z)

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

flags = cv2.KMEANS_RANDOM_CENTERS

compactness, labels, centers = cv2.kmeans(z, 2, None, criteria, 10, flags)

print(compactness)
print(labels)
print(centers)

A = z[labels == 0]
B = z[labels == 1]

plt.hist(A,256,[0,256],color = 'r')
plt.hist(B,256,[0,256],color = 'b')
plt.hist(centers,32,[0,256],color = 'y')
plt.show()


