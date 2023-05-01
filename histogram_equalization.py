import cv2
from matplotlib import pyplot as plt

#グレースケールで画像を読み込む
img = cv2.imread('image/Lenna.jpg', 0)

#ヒストグラムを計算
hist_img = cv2.calcHist([img], [0], None, [256], [0, 255])

#ヒストグラム平坦化を画像に適用
equalized = cv2.equalizeHist(img)

#ヒストグラムを計算
hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 255])

#２行２列の領域に、下記の４つをそれぞれ描画
#１番目（左上）に、入力画像を描画
plt.subplot(221)
plt.imshow(img, 'gray')

#２番目（右上）に、ヒストグラム平坦後の画像を描画
plt.subplot(222)
plt.imshow(equalized, 'gray')

#３番目（左下）に入力画像のヒストグラムを描画
plt.subplot(223)
plt.plot(hist_img), plt.title('original')

#４番目（右下）にヒストグラム平坦後の画像のヒストグラムを描画
plt.subplot(224)
plt.plot(hist_equalized)
plt.title('equalized')

plt.show()
