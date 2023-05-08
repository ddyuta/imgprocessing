import cv2

capture = cv2.VideoCapture('image/sample30fps.mp4')
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)



print('frame size = ' + str(width) + 'x' + str(height))
print('fps = ' + str(fps))
print('frame count = ' + str(frame_count))
print('playing time = ' + str(frame_count / fps))
