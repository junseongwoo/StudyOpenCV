import cv2

image = cv2.imread("dog.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("사진 에러")

'''
cv2.flip(입력, 배열 뒤짚는 축) : 수직, 수평, 양축으로 뒤짚는다 각각 0, 1, -1

cv2.repeat(입력, 수직방향, 수평방향 반복횟수) : 입력 이미지를 반복하여 출력

cv2.transpose(입력) : 가로와 세로 방향을 바꿈
'''

x_axis = cv2.flip(image, 0)
y_axis = cv2.flip(image, 1)
xy_axis = cv2.flip(image, -1)
rep_img = cv2.repeat(image, 2, 2)
trans_img = cv2.transpose(image)

titles = ["image", "x_axis", "y_axis", "xy_axis", "rep_img", "trans_img"]
for title in titles:
    cv2.imshow(title, eval(title))

cv2.waitKey(0)
cv2.destroyAllWindows()