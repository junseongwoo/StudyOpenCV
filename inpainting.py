# inpainting 오래된 사진에서 작은 노이즈를 제거 하는 방법 

# 노이즈 부분을 주변 픽셀들로 대체 -> 주변부처럼 자연스레 보이도록 하는 것 

'''
    basic
    이미지 인페인팅 : 노이즈 부분을 주변 픽셀들로 대체하여 주변부처럼 자연스레 보이도록 하는 것 

    cv2.inpaint()로 구현 가능 
    
'''

import cv2
import numpy as np 

noise_img = cv2.imread('./images/img1.png')
noise_img = cv2.resize(noise_img, (480, 480))
noise = cv2.imread('./images/img2.png')

noise = cv2.cvtColor(noise, cv2.COLOR_BGR2GRAY)
noise = cv2.resize(noise, (480, 480))

dst = cv2.inpaint(noise_img, noise, 3, cv2.INPAINT_TELEA)

cv2.imshow('python', noise_img)
cv2.imshow('noise', noise)
cv2.imshow('inpaint', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()