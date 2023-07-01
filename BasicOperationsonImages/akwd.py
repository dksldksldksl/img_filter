#import cv2 as cv
#img = cv.imread('C:/Users/user/Documents/dev/LSG/img_filter/BasicOperationsonImages/messi5.jpg')
#assert img is not None, "file could not be read, check with os.path.exists()"
#lower_reso = cv.pyrDown(img)
#higher_reso2 = cv.pyrUp(lower_reso)

#mport numpy as np
#import cv2 as cv
#im = cv.imread('C:/Users/user/Documents/dev/LSG/img_filter/BasicOperationsonImages/messi5.jpg')
#assert im is not None, "file could not be read, check with os.path.exists()"
#imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#ret, thresh = cv.threshold(imgray, 127, 255, 0)
#contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#cnt = contours[4]
#cv.drawContours(im, [cnt], 0, (255,255,0), 500)
#cv.imshow('dst', im)
# im을 저장하는 함수 호출 
#cv.waitKey()
# cv.imwrite('./after.png',im)

import cv2 as cv
import numpy as np

im = cv.imread('C:/Users/user/Documents/dev/LSG/img_filter/BasicOperationsonImages/hi.PNG')
assert im is not None, "file could not be read, check with os.path.exists()"

img_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 127, 255, 0)

contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

hull = cv.convexHull(cnt, returnPoints=False)
defects = cv.convexityDefects(cnt, hull)

if defects is not None:
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        cv.line(im, start, end, [0, 255, 0], 2)
        cv.circle(im, far, 5, [0, 0, 255], -1)

cv.imshow('img', im)
cv.waitKey(0)
cv.destroyAllWindows()
