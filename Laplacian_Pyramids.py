import cv2 
import numpy as np

img = cv2.imread('./images/lena.jpg')

Down_img = cv2.pyrDown(img)
Down_to_Upimg = cv2.pyrUp(Down_img)

laplacian = cv2.subtract(img, Down_to_Upimg)

restored = laplacian + Down_to_Upimg 

images = [img, Down_to_Upimg, laplacian, restored]

merged = np.hstack(images)
cv2.imshow('Laplacian Pyramid', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
