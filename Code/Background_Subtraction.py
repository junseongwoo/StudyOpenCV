# 배경제거 

import cv2
import numpy as np 

cap = cv2.VideoCapture('./images/walking.avi')

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while (1):
    ret, frame = cap.read()
    frame = cv2.resize(frame,(400,400))
    fgmask = fgbg.apply(frame)
    cv2.imshow('original',frame)
    cv2.imshow('MOG2',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()