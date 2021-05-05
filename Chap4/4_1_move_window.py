import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)         # (200행, 400열)이고 원소가 전부 0인 행렬 생성
image[:] = 200                                 # 밝은 회색 바탕 영상 생성

title1, title2 = 'Position1', 'Position2'      # 윈도우 이름 설정

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)   # 윈도우 생성 및 크기 조정 옵션
# WINDOW_AUTOSIZE이기 때문에 image의 행렬과 같은 크기의 윈도우가 생성된다.
cv2.namedWindow(title2)
cv2.moveWindow(title1, 250, 800)               # 윈도우 위치 지정
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)                      # 행렬을 영상으로 표시
cv2.imshow(title2, image)

cv2.waitKey(0)                                 # 키 이벤트 : 아무키나 누르면 꺼짐
cv2.destroyAllWindows()
