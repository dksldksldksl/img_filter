# **📂이미지 그리기**

## 이미지 불러 오기

```py
import numpy as np
import cv2 as cv
```

---

##  검정색 이미지 만들기

```py
img = np.zeros((512,512,3), np.uint8)
```

---

## ✏️ Draw a diagonal blue line with thickness of 5 px

```py
cv.line(img,(0,0),(511,511),(255,0,0),5)
```
---

## ✏️두께가 5인 파란색 대각선 그리기

```py
cv.line(img,(0,0),(511,511),(255,0,0),5)
```
---

## ✏️사각형 그리기

```py
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
```
---

## ✏️원그리기

```py
cv.circle(img,(447,63), 63, (0,0,255), -1)
```
---
## ✏️타원 그리기

```py
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
```
---
## ✏️다각형 그리기

```py
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
```
---
## 📟  윈도우 창에 이미지 표시
```py
cv.imshow("draw", img)
```
---
## 📰 아무 키나 누를때 까지 대기
```py
cv.waitKey(0)
```