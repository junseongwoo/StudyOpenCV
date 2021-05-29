# StudyOpencv
OpenCV 학습 리포지토리 

	
6일차

resize(1, 2, 3, 4, 5) 함수
  - 1 : 처리할 대상
  - 2 : 조정할 이미지의 크기
  - 3, 4 : 각각 y축, x축으로 조정할 scale(크기) 설정
  - 5 : 보간(interpolation), 이미지의 크기를 조정함에 따라 각 픽셀의 정보 보간법(줄어들거나, 커졌을 때 픽셀간의 값을 어떻게 채울 것인지)
      - cv2.INTER_AREA : 지역 보간
      - cv2.INTER_CUBIC : cubic 보간
      - cv2.INTER_LINEAR : 선형 방식으로 보간(기본설정)
 
Image Filtering
  - 이미지에 존재하는 픽셀을 해당하는 픽셀의 주위에 있는 픽셀들을 활용한 특정한 함수를 적용한 결과를 기반으로 수정하는 개념
  - mask 생성 후 이 mask를 기준으로 주변값들을 생성

 cv2.blur(image, destination ,커널 사이즈 [anchor type, border type])

 
피라미드 기법(pyramid)
  - Level 0 : Original Size
  - Level 1 
     - up : (image size)*2
     - down : (image size)*0.5

 
피라미드 업(pyramid up)
  - 원래 이미지의 크기를 2배 늘림
  - 이미지의 샘플링을 크게 하고 blur 처리


피라미드 다운(pyramid down)
  - 원래 이미지의 크기를 1/2로 줄임
  - 이미지의 샘플링을 작게하고 blur 처리

 
피라미드 연산의 장점
  1. 낮은 해상도
  2. 다양한 이미지의 크기 처리 
  3. 쉬운 이미지 처리
  4. edge를 쉽게 찾을 수 있음

이미지 처리(Arithmetic 연산)
  - Image Addiction
  - Image Blending
     - 이미지들의 합
     - 이미지가 겹쳐보이게 하거나 투명하게 보이게 하는 방법
     - y = image1 * (1 - 특정가중치) + (image2 *  특정가중치) / 특정가중치
     - 특정가중치 : 0~1 사이의 값
  - Image Substrction
  - Bit Operation
     - masking에 도움을 줌
     - AND, OR, XOR, NOT 연산 사용

 Image translation
  - 이미지의 객체나 위치를 옮기는데 사용
  - (x, y) 방향으로 옮김
  - 옮겨진 장소 : (tx, ty)
  - transformation matrix M = [ [1 0 tx] [0 1 ty] ]

 

Image Rotation(Roration Transformation)
  - 이미지 축 변경
  - 변경할 각도 지정
  - transformation matrix M = [ [cos -sin] [sin cos] ]
  - OpenCV scaled rotation

 Log Transformation
  - 이미지 개선에 사용
  - gray 수준 변환 중 하나
  - 모든 픽셀의 값을 로그 값으로 변경
  - 이미지의 어두운 색을 가진 픽셀을 밝게 변경
  - 일반적으로 어두운 계열의 이미지에 적용
  - result = c * log(1 + r)
     - r = 입력 픽셀값
     - c = scaling(증폭, 확장)시킬 값
     - c = 255 / (log(1 + 입력한 픽셀값 중 최대값))

Power Law Transformation or Gamma Correction(감마 보정)
  - 이미지 개선에 사용
  - 출력 장비의 차이를 보정해주는 방법
  - s = c * r의 gamma 제곱(**)
     - s : 계산값
     - r : 입력값
     - c : scaling(증폭, 확장)시킬 값
     - gamma : 음수가 아닌 상수값

 Image Segmantation
  - Image Classification -> Image Object Detection -> Imgae Segmentation

 ROI
  - Region of Interest (in computer vision)
  - Return of Investment (in economics)

7일차

Image Thresholding
  - 시각적 데이터의 단순화
  - 이미지 세그먼테이션(Image Segmentation) 가능
  - 이미지를 구성하는 픽셀에 2 가지 수준을 할당하는 개념(특정 threshold 값 기준)
  - 픽셀 값이 threshold 보다 높으면 white, 낮으면 black 할당

Threshold의 종류
  - Simple Thresholding
  - Adaptive Thresholding
    - 이미지의 특정 부분 색 보정
    - 다른 부분에 다른 방법 적용
       : 알고리즘이 threshold 계산 -> 각기 다른 임계차 적용

Blur
 : 이미지를 단순화하는 동시에 노이즈 제거
 
Noise
 : 이미지에 존재하는 픽셀의 원래값이 아닌 밝기나 색의 변종
 
이미지에 노이즈가 생길 수밖에 없는 이유
  - 이미지의 전기적 전송(카메라 - 네트워크 - ...)
  - 센서에 문제가 생기거나 조정이 일어났을 경우
  - 빛의 강도 ISO Factor

Noise의 종류
  - Impulse
  - Gaussian
  - Poisson
  - Speckle

Image Gradients
  - 이미지 선명도(sharpness) 측정
  - 이미지의 선명도(sharpness)가 클수록 더 높은 gradients를 가진다

Edge(모서리)
  - 이미지에서 갑자기 끊겨지는 변화
  - 이미지에서 갑자기 과도하게 변경되는 부분
  - 서로 다른 segmentation과 같은 구분

Edge Detection
  1) 실행 이유
    - 모양의 정보를 얻기 위함
    - Feature Extraction(특성 추출)
    - 패턴 인식
    - 이미지 형태 변형
  2) 실행 방법
    - Sobel
    - Prewitt
    - Laplacian
    - Canny
  3) Canny Edge Detection
    - 가장 효과적이지만 복잡한 방법
    - 과정
       - 필터를 통해 smooth noise를 제거하거나 매끈하게 만들어준다. -- gaussian filter
       - gradient 연산을 통해 gradient 계산
       - edge point 모서리 지점 추출
       - egde point들을 연결
