import cv2
import statistics
from matplotlib import pyplot as plt

#グレースケールで画像を読み込む
img = cv2.imread('image/Lenna.jpg', 0)

#ヒストグラムを計算し、描画
plt.hist(img.ravel(), 256,[0, 255])

#16個のBINでのヒストグラムを計算し、描画
#plt.hist(img.ravel(), 16, [0, 255])

plt.show()

#最頻値の値を出力
print(statistics.mode(img.ravel()))
