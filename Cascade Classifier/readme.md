## 이미지 불러오기
```py
import numpy as np
import cv2 as cv
```
## 이미지 파일 'chessboard.png'를 읽어와서 그레이스케일로 변환
```py
filename = './Cascade Classifier/images.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
```
## 그레이스케일 이미지를 float32 데이터 타입으로 변환하고, Harris 코너 검출 알고리즘을 적용하여 코너를 검출하는 코드
```py
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
```
## 코너 검출 결과 이미지인 dst에 대해 연산을 수행하는 코드
```py
dst = cv.dilate(dst,None)
```git clone MY_PROJECT_LINK


## 주어진 코드는 코너 검출 결과에서 임계값을 기준으로 코너 지점을 선택하고 해당 지점을 원본 이미지에서 빨간색으로 표시하여 보여주는 코드
```py
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
```
## 키를 누를 때까지 결과를 화면에 보여줌
```py
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
```