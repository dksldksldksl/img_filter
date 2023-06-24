import cv2

grayImg = cv2.imread("C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\load_img\\img\\background.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite('C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\save_img\\img\\gray.jpg', grayImg)
cv2.imshow('gray', grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()