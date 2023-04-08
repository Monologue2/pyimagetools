import cv2

cap1 = cv2.VideoCapture('videos/hazy.avi')
cap2 = cv2.VideoCapture('videos/hazy_aicon.mp4')
cap3 = cv2.VideoCapture('videos/hazy_ai.avi')
cap4 = cv2.VideoCapture('videos/manual.h264')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
img_array = []
cap5 = cv2.VideoWriter('videos/cat.mp4', fourcc, 15, (1920*2, 1080*2))
cnt = 0
while True:
  ret1, frame1 = cap1.read()
  ret2, frame2 = cap2.read()
  ret3, frame3 = cap3.read()
  ret4, frame4 = cap4.read()
  cnt += 1
  print(cnt, end="\r")
  if not ret1:
    print(1)
    break
  if not ret2:
    print(2)
    break
  if not ret3:
    print(3)
    break
  if not ret4:
    print(4)
    break
  img_h1 = cv2.hconcat(frame1, frame2)
  img_h2 = cv2.hconcat(frame3, frame4)
  img_v = cv2.vconcat(img_h1, img_h2)
  cap5.write(img_v)
cap5.release()