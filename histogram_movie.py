import cv2
from matplotlib import pyplot as plt
import statistics

#動画の読み込み
capture = cv2.VideoCapture('image/sample30fps.mp4')
#BGRそれぞれでヒストグラムを作成するために、ループ用tupleを作成
color = ('b', 'g', 'r')
fig = plt.figure()

if not capture.isOpened():
    print('動画ファイルを開けませんでした')
    exit()
#’e’を押した時にプログラムを終了する関数
def press(event):
    if event.key == 'e':
        capture.release()
        cv2.destroyAllWindows()
        plt.close()
        exit()

while True:
    ret, frame = capture.read()
    if ret:
        cv2.imshow('frame', frame)

        plt.clf()
        for i, col in enumerate(color):
            #ヒストグラムを計算
            histr = cv2.calcHist([frame], [i], None, [256], [0, 255])
            #ヒストグラムを描画
            plt.plot(histr, color=col)


        #x軸とy軸の範囲を指定
        plt.xlim([0, 255]), plt.xlabel('pixel_value')
        plt.ylim([0, 20000]), plt.ylabel('pixel_of_number')

        #ヒストグラムを描画
        plt.pause(0.01)

        #print(statistics.median(frame.ravel()))
        #print(statistics.mean(frame.ravel()))

        #’ｑ’を押したときにbreak
        #この書き込みがないと映像が表示されない
        k = cv2.waitKey(1) & 0Xff
        if k == ord('q'):
            break
        #press関数を使用し、’e’を押したときにプログラム終了
        fig.canvas.mpl_connect('key_press_event', press)

    else:
        break

capture.release()
cv2.destroyAllWindows()
