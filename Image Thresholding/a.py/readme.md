## 필요한 모듈 불러오기
```py
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
```
## 이미지 불러오기
```py
img = cv.imread('C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\load_img\\img\\background.jpg', cv.IMREAD_GRAYSCALE)
```
## 파일이 열리지 않을때 file could not be read, check with os.path.exists()을 오류 라고함
```py
assert img is not None, "file could not be read, check with os.path.exists()"
```
## 이미지에 중간값 블러를 적용하여 이미지를 부드럽게 만드는 역할
```py
img = cv.medianBlur(img,5)
```
## 이미지를 이진화하여 th1 변수에 저장
```py
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
```
##  적응형 임계값을 사용하여 이미지를 이진화하여 th2 변수에 저장
```py
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
 cv.THRESH_BINARY,11,2)
```
## 이진화된 이미지를 가우시안 적응 임계처리하여 th3 변수에 저장하는 코드
```py
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
 cv.THRESH_BINARY,11,2)
```
참고 :  https://mr-waguwagu.tistory.com/15

## 이미지들의 제목과 해당 이미지들을 매핑하여 리스트로 저장
```py
titles = ['Original Image', 'Global Thresholding (v = 127)',
 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
```
##
 이미지들을 2x2의 서브플롯에 순서대로 시각화하여 출력
```py
for i in range(4):
 plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
 plt.title(titles[i])
 plt.xticks([]),plt.yticks([])
plt.show()
```