### 이미지 불러오기
```py
import cv2 as cv
img1 = cv.imread('C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\Arithmetic Operations on Images\\maxresdefault (1).jpg')
img2 = cv.imread('C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\Arithmetic Operations on Images\\maxresdefault.jpg')
```
### 이미지 파일을 불러오는데 실패하면 오류를 발생시키는 코드&파일을 읽을 수 없는 경우에는 os.path.exists()를 사용
```py
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
```
### img1'과 'img2' 이미지를 각각 가중치 1.0과 0.9로 섞어서 합치고 마지막 파라미터인 0은 추가적인 스칼라 값을 더하지 않고 이미지들만 가중합하는 것
```py
dst = cv.addWeighted(img1,1.0,img2,0.9,0)
```
###  이미지를 보여주고 키 입력을 대기, 창을 닫을 때까지 유지하는 코드 'dst'라는  이미지를 보여주고 cv.waitKey(0)를 통해 키 입력을 대기 그 후 cv.destroyAllWindows()를 호출하여  이미지 창을 닫음

```py
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
```
