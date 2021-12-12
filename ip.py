'''
Descripttion: 
version: 
Author: LiQiang
Date: 2021-01-24 12:31:01
LastEditTime: 2021-01-24 14:07:39
'''
# -*- coding: utf-8 -*-
import cv2
import sys
#手机软件名：ip摄像头
# 根据摄像头设置IP及rtsp端口
# url='rtsp://admin:admin@192.168.0.104:8554/live'
url='http://admin:admin@192.168.0.104:8081'
 
# 读取视频流
cap = cv2.VideoCapture(url)
# 设置视频参数
cap.set(3, 480)
 
print(cap.isOpened())
 
print(sys.version)
 
print(cv2.__version__)
 
while cap.isOpened():
    ret_flag, img_camera = cap.read()
    cv2.imshow("camera", img_camera)
 
    # 每帧数据延时 1ms, 延时为0, 读取的是静态帧
    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite("test.jpg", img_camera)
    if k == ord('q'):
        break
 
# 释放所有摄像头
cap.release()
 
# 删除窗口
cv2.destroyAllWindows()
 
 