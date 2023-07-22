import cv2 as cv
import sys

# image 불러오기 : cv.imread()
img = cv.imread(cv.samples.findFile("C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\Gui Features in OpenCV\\Getting Started with Images\\background.jpg"))

# image가 제대로 불러와졌는지 확인
if img is None:
    sys.exit("Could not read the image.")

# image show
cv.imshow("Akalli", img)

# 키보드 입력 대기 및 키보드 입력 시 k로 대입
k = cv.waitKey(0)

# 입력 받은 키가 s라면 이미지 저장하기
if k == ord("s"):
    cv.imwrite("C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\Gui Features in OpenCV\\Getting Started with Images\\background.png", img)