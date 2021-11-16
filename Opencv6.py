import cv2

cv2.namedWindow('demo', cv2.WINDOW_NORMAL)
cv2.resizeWindow('demo', 640, 380)

# img = cv2.imread('./img/1.png')
# cap = cv2.VideoCapture(0)

#直接读取视频
cap = cv2.VideoCapture('./img/box.mp4')
while True:
    ret, frame = cap.read()
    cv2.imshow('demo', frame)
     # 此处不能设为1，否则会过快，可以设的比播放视频每秒帧数长一点
    key = cv2.waitKey(40)
    if key & 0xFF == ord('q'):
        break
    # 解决openCV打开的窗口点击了X关闭 却不能关闭的问题
    if cv2.getWindowProperty('demo', cv2.WND_PROP_VISIBLE) <1:
        break
# cv2.imshow('demo', img)
# key = cv2.waitKey(0)
# if key == 'q':
#     exit()

cap.release()
cv2.destroyAllWindows()