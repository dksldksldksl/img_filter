import numpy as np
import cv2 as cv
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_MOUSEMOVE:
        cv.circle(img,(x,y),20,(255,0,0),-1)
    if event == cv.EVENT_LBUTTONUP:
        size = 40
        cv.rectangle(img,(x-size, y-size),(x+size, y+size),(0,255,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()