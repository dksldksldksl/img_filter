## 이미지 불러오기
import numpy as np
import cv2 as cv
## 마우스 따라가는 함수 & 따라가면서 파랑색,초록색 네모 칠하기 

```PY
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_MOUSEMOVE:
        cv.circle(img,(x,y),20,(255,0,0),-1)
    if event == cv.EVENT_LBUTTONUP:
        size = 40
        cv.rectangle(img,(x-size, y-size),(x+size, y+size),(0,255,0),-1)
```

## 검정색 이미지 만들기
```py
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
```

## 이미지 무한 표시&ESC을 누르면 꺼지기
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()