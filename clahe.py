import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/Lenna.jpg', 0)

#ヒストグラムを計算
hist_img = cv2.calcHist([img], [0], None, [256], [0, 255])

#ヒストグラム平坦化を画像に使用
equalized = cv2.equalizeHist(img)

#ヒストグラムを計算
hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 255])

#CLAHE（コントラクト制限付き適応的ヒストグラム平坦化）インスタンスを作成
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

#CLAHEを画像に適用
clahe_img = clahe.apply(img)

#ヒストグラムを計算
hist_clahe = cv2.calcHist([clahe_img], [0], None, [256], [0, 255])

#２行３列の領域に、下記６つをそれぞれ描画
#左上入力画像
plt.subplot(231), plt.imshow(img, 'gray')

#中央上ヒストグラム平坦後の画像
plt.subplot(232), plt.imshow(equalized, 'gray')

#右上適応型ヒストグラム平坦後の画像
plt.subplot(233), plt.imshow(clahe_img, 'gray')

#左下入力画像のヒストグラム
plt.subplot(234), plt.plot(hist_img), plt.title('original')

#中央下ヒストグラム平坦後画像
plt.subplot(235), plt.plot(hist_equalized), plt.title('equalized')

#右下適応型ヒストグラム平坦後画像
plt.subplot(236), plt.plot(hist_clahe), plt.title('clahe')


plt.show()
