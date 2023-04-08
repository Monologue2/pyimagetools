import cv2
import numpy as np
import os

#clear code
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# cap2 = cv2.VideoWriter('results/clear.avi', fourcc, 15, (720, 480))

# filenames = os.listdir('./tmp/manual')
# filenames.sort()
# for filename in filenames:
#     cap = cv2.imread(f"./{filename}")
#     cap = cv2.resize(cap, dsize=(720, 480), interpolation=cv2.INTER_AREA)
#     cap2.write(cap)
# cap2.release()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
filenames = os.listdir('./tmp/manual')
filenames.sort()
#cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=None)
cap2 = cv2.VideoWriter('./tmp.avi', fourcc, 15, (720, 480))
cnt = 0
for filename in filenames:
    cnt += 1
    print(cnt, filename)
    cap = cv2.imread(f"./tmp/manual/{filename}")
    # cap = cv2.imread(f"./real/{cnt}.jpg")
    # cap = cv2.resize(cap, dsize=(1280, 720), interpolation=cv2.INTER_AREA)
    cap2.write(cap)
cap2.release()