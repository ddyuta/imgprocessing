import cv2
import numpy as np

#何も処理しないコールバック関数を作成
def nothing(x):
    pass

#黒い画像を作成
img = np.zeros((300,512,3), np.uint8)

#画像を表示するウィンドウを作成
cv2.namedWindow('image')
#BGR色空間で色を変更するトラックバーを作成
cv2.createTrackbar('Blue', 'image', 0, 255, nothing)
cv2.createTrackbar('Green', 'image', 0, 255, nothing)
cv2.createTrackbar('Red', 'image', 0, 255, nothing)

#HSV色空間で色を変更するトラックバーを作成
cv2.createTrackbar('Hue', 'image', 0, 179, nothing)
cv2.createTrackbar('Saturation', 'image', 0, 255, nothing)
cv2.createTrackbar('Value', 'image', 0, 255, nothing)

#ON時にBGR色空間の色を表示、OFF時にHSV色空間の色を表示する制御を実施するトラックバーを作成
cv2.createTrackbar('switch', 'image', 0, 1, nothing)

while True:
    switch = cv2.getTrackbarPos('switch', 'image')

#スイッチがONの場合はBGR色空間の色を表示
    if switch == 1:

#トラックバーの値を取得
        b = cv2.getTrackbarPos('Blue', 'image')
        g = cv2.getTrackbarPos('Green', 'image')
        r = cv2.getTrackbarPos('Red', 'image')

#BGRの値を画像に代入
        img[:] = [b, g, r]

#スイッチがOFFの場合はBGR色空間の色を表示
    else:

#トラックバーの値を取得
        h = cv2.getTrackbarPos('Hue', 'image')
        s = cv2.getTrackbarPos('Saturation', 'image')
        v = cv2.getTrackbarPos('Value', 'image')
        
#HSVの値を画像に代入
        img[:] = [h, s, v]
        img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    k = cv2.waitKey(1) & 0xFF

#'c'を押下した際に現在表示している色をBGRとHSV間で変換した際の値を出力
    if k == ord('c'):
        
#スイッチがONの場合はBGR色空間の色をHSV色空間に変換した値を表示
        if switch == 1:
            value = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            print(value[0, 0])

#スイッチがOFFの場合はHSV色空間の色をBGR色空間に変換した値を表示
        else:

#BGR値に変換した値をimgに代入しているため、画素から取得しprint
            print(img[0, 0])

#'q'を押下した際にbreak
    elif k == ord('q'):
        break

    cv2.imshow('image', img)

cv2.destroyAllWindows()
