'''
원본 이미지의 모든 직선은 출력 이미지에서 직선으로 유지 
입력 이미지의 네 점과 대응하는 출력 이미지의 네 점이 필요 
두 이미지 간에 대응하는 네 점을 안다면 getAffineTransform 함수 사용하여 변환 행렬을 얻음 
wrapAffine 함수를 사용하여 이미지에 적용 
'''

import numpy as np  
import cv2 

# 마우스 클릭한 좌표를 저장할 리스트 
src = np.zeros([4,2], dtype = np.float32)
idx = 0 

def mouse_callback(event, x, y, flags, param):
    global point_list, idx 

    # 마우스 왼쪽 버튼을 누를 때 마다 좌표를 리스트에 저장 
    if event == cv2.EVENT_LBUTTONDOWN:
        src[idx] = (x,y)
        idx = idx + 1 
        print("(%d, %d)"%(x,y))

        cv2.circle(img_color, (x,y), 10, (0,0,255),-1)

# 마우스 콜백함수를 등록 
cv2.namedWindow('original')
cv2.setMouseCallback('original', mouse_callback)

# 사용할 이미지를 불러온다 
img_color = cv2.imread('../StudyOpenCV/images/sudoku_test.jpg')
img_color = cv2.resize(img_color, (600, 600))
img_original = img_color.copy() 

# 반복하면서 네 점을 지정하도록 함
while(True):
    cv2.imshow('original', img_color)

    height, width = img_color.shape[:2]

    if cv2.waitKey(1) == 32:
        break 

# 퍼스팩티브 변환 후 영역으로 사각 영역을 지정 
dst = np.float32([[0,0], [width, 0], [0, height], [width, height]])

# 퍼스펙티브 변환 행렬 생성
M = cv2.getPerspectiveTransform(src, dst)

# 이미지에 퍼스펙티브 변환 적용
img_result = cv2.warpPerspective(img_original, M, (width, height))

cv2.imshow('result', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
