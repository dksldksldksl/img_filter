## 이미지 불러 오기
```py
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
```
## img 변수에 저장하며, 파일을 읽을 수 없는 경우에는 오류 메시지를 출력하는 역할
```py
img = cv.imread('C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\save_img\\img\\background.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
```
## th1 변수에 결과를 저장   저장 임계값은 127로 설정되고 이진화 결과는 0과 255로 구성된 이미지가 th1 변수에 저장
```py
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
```
## 이미지에 Otsu의 이진화를 적용하여 임계값과 이진화된 이미지를 반환
```py
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
```

# Otsu의 이미지를 이진화
```py
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
```
## 이미지의 이진화된 결과를 리스트에 저장하는 작업
```py
images = [img, 0, th1,
 img, 0, th2,
 blur, 0, th3]
 ```
 ## 이미지들의 제목을 리스트에 저장하는 작업을 수행합니다.
 ```py
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
 'Original Noisy Image','Histogram',"Otsu's Thresholding",
 'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
 ```
 ## 코드는 이미지와 해당 이미지의 제목을 서브플롯으로 그려주는 작업을 수행
 ```py
for i in range(3):
 plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
 plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
 plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
 plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
 plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
 plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
 ```