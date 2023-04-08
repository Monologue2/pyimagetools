import cv2
import numpy as np
# import requests
import os

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
cap = cv2.VideoCapture('tmp.h264')
# cap = cv2.VideoCapture('results/dfbDAU.avi')
cnt = 0
while True:
    print(cnt, end='\r')
    cnt += 1
    retval, frame = cap.read()
    # cv2.imshow(f"{cnt}", frame)
    # cv2.waitKey()
    if not(retval):
        print("end")
        break
    cv2.imwrite(f'./tmp/manual/{cnt}.jpg', frame)