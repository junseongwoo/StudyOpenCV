import numpy as np
import cv2
cap = cv2.VideoCapture('./images/walking.avi')

while(1):
    ret ,frame = cap.read()
    if ret == True:
        cv2.imshow('original',frame)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
