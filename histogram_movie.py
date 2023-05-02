import cv2
from matplotlib import pyplot as plt

#'e'を押し下した際にプログラムを終了する関数
def press(event):
    if event.key == 'e':
        capture.release()
        cv2.destroyAllWindows()
        plt.close()
        exit()

capture = cv2.VideoCapture('image/sample.mp4')

#BGRそれぞれでヒストグラムを作成するために、ループ用tupleを作成
color = ('b', 'g', 'r')

fig = plt.figure()

while True:
    ret, frame = capture.read()
    cv2.imshow('frame', frame)# cv2.imshow('frame', frame)
    if ret:
        #ヒストグラムの初期化
        plt.clf()
        for i, col in enumerate(color):
            #ヒストグラムを計算
            histr = cv2.calcHist([frame], [i], None, [256], [0, 255])
            #ヒストグラムを描画
            plt.plot(histr, color=col)
        #ｘ軸を0-255、ｙ軸を0-20000の範囲で表示
        plt.xlim([0, 255])
        plt.ylim([0,20000])
        #ヒストグラムを描画
        plt.pause(0.01)
        #動画を表示
        cv2.imshow('frame', frame)
        #press関数を使用し、'e'を押し下した際にプログラムを終了
        fig.canvas.mpl_connect('key_press_event', press)

    else:
        break

capture.release()
cv2.destroyAllWindows()
