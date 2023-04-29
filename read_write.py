import cv2

img = cv2.imread('image/Lenna.jpg')

cv2.imwrite('image/read_write.jpg', img)

