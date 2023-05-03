import cv2
import time

capture = cv2.VideoCapture('image/sample30fps.mp4')

#
if not capture.isOpened():
    print('動画ファイルを開けませんでした')
    exit()

while True:
    ret, frame = capture.read()
    if ret:
        cv2.imshow('frame', frame)
        time.sleep(0.025)

        #
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break

    else:
        break

capture.release()
cv2.destroyAllWindows()
