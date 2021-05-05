import numpy as np
import cv2

# 스위치 케이스문을 딕셔너리형으로 구현했다.
switch_case = {
    ord('a'): "a키 입력",                # a,b 를 아스키코드로 변경해서 키값을 저장, 키보드가 눌러지면 해당 문자의 아스키 코드로 반환하기 떄문
    ord('b'): "b키 입력",
    0x41: "A키 입력",
    int('0x42', 16): "B키 입력",
    2424832: "왼쪽 화살표키 입력",
    2490368: "윗쪽 화살표키 입력",
    2555904: "오른쪽 화살표키 입력",
    2621440: "아래쪽 화살표키 입력"
}

image = np.ones((200, 300), np.float)
cv2.namedWindow('Keyboard Event')
cv2.imshow("Keyboard Event", image)

while True:
    key = cv2.waitKeyEx(100)             # 100ms 동안 키 이벤트 대기
    if key == 27:                        # esc 키 누르면 종료
        break

    try:                                 # try - except 문으로 사전에 있는 문자가 아니면 표시가 안되게 함
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()