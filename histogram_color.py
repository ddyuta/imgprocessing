import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image/Lenna.jpg')

#BGRそれぞれでヒストグラムを作成するために、ループ用tupleを作成
color = ('b', 'g', 'r')


for i, col in enumerate(color):

    #ヒストグラムを計算
    histr = cv2.calcHist([img], [i], None, [256], [0, 255])

    #ヒストグラムを描画
    plt.plot(histr, color=col)

#x軸を0-255の範囲で表示
plt.xlim([0, 255])
#y軸を0-250の範囲で表示
plt.ylim([0, 2500])
plt.show()
