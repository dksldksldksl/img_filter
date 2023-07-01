import cv2 as cv

img = cv.imread ( 'C:\\Users\\user\\Documents\\dev\\LSG\\img_filter\\Basic Operations on Images\\messi5jpg.jpg' )
assert img is  not  None , "파일을 읽을 수 없습니다. os.path.exists()로 확인하십시오."
px = img[100,100]
print( px )

blue = img[100,100,0]
print( blue )
img[100,100] = [255,255,255]
print( img[100,100] )

# accessing RED value
img.item(10,10,2)

# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

high_reso2 = cv.pyrUp (lower_reso)