import cv2
import numpy as np

if __name__ == "__main__":

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # 25为帧率，(1280, 720)为分辨率，该分辨率必须与设备摄像头分辨率保持一致
    vw = cv2.VideoWriter("/Users/admin/Documents/out.mp4", fourcc, 25, (1280, 720))
    # 创建窗口
    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('video', 640, 480)
    # 获取摄像头资源
    cap = cv2.VideoCapture(0)
    # 判断摄像头是否打开
    while cap.isOpened():
        # 从摄像头读视频桢
        ret, frame = cap.read()
        if ret:
            # 将视频帧在窗口中显示
            cv2.imshow('video', frame)
            # 写数据到多媒体文件
            vw.write(frame)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break
        else:
            break
    # 释放资源
    cap.release()
    vw.release()
    cv2.destroyAllWindows()