import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/lena.jpg')

Upimg = cv2.pyrUp(img)
Downimg = cv2.pyrDown(img)

plt.subplot(1,3,1)
plt.imshow(img)
plt.title('Original Img')

plt.subplot(1,3,2)
plt.imshow(Upimg)
plt.title('Upsampling Img')

plt.subplot(1,3,3)
plt.imshow(Downimg)
plt.title('Downsampling Img')
plt.show()