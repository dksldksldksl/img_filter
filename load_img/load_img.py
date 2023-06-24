import cv2

image = cv2.imread("C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\load_img\\img\\background.jpg",cv2.IMREAD_ANYCOLOR)

cv2.imshow("Universe",image)
cv2.waitKey(0)
cv2.destroyAllWindows()