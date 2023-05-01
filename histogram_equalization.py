import cv2
from matplotlib import pyplot as plt

#
img = cv2.imread('image/Lenna.jpg', 0)

#
hist_img = cv2.calcHist([img], [0], None, [256], [0, 255])

#
equalized = cv2.equalizeHist(img)

#
hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 255])

#
#
plt.subplot(221)
plt.imshow(img, 'gray')

#
plt.subplot(222)
plt.imshow(equalized, 'gray')

#
plt.subplot(223)
plt.plot(hist_img), plt.title('original')

#
plt.subplot(224)
plt.plot(hist_equalized)
plt.title('equalized')

plt.show()
