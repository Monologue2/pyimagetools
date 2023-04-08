import cv2
import numpy as np
# import requests
import os

# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# cap2 = cv2.VideoWriter('results/clear.avi', fourcc, 15, (720, 480))

# filenames = os.listdir('./clear')
# filenames.sort()
# for filename in filenames:
#     cap = cv2.imread(f"./clear/{filename}")
#     cap = cv2.resize(cap, dsize=(720, 480), interpolation=cv2.INTER_AREA)
#     cap2.write(cap)
# cap2.release()


# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# filenames = os.listdir('./tmp/manual')
# filenames.sort()
# cap2 = cv2.VideoWriter('results/tmp.avi', fourcc, 15, (512, 512))
# cnt = 0
# for filename in filenames:
#     cnt += 1
#     print(cnt, filename)
#     cap = cv2.imread(f"./tmp/manual/{filename}")
#     # cap = cv2.imread(f"./real/{cnt}.jpg")
#     # cap = cv2.resize(cap, dsize=(1280, 720), interpolation=cv2.INTER_AREA)
#     cap2.write(cap)
# cap2.release()






# session = requests.Session()

# tmp = session.get("http://115.22.184.227:8080/seafog/seafogList.do?modelCode=SeaFog_Daesan&startDate=202107061000&endDate=202107061959").json()

# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# img_array = []
# cap2 = cv2.VideoWriter('results/daesan_vid.avi', fourcc, 15, (720, 480))

# for val in tmp["seafogList"]:
#     print("http://115.22.184.227:8080" + val["file_path"])
#     image_nparray = np.asarray(bytearray(session.get("http://115.22.184.227:8080/" + val["file_path"]).content), dtype=np.uint8)
#     cap = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
#     # cap = cv2.imread("http://115.22.184.227:8080" + val["file_path"])

#     cap = cv2.resize(cap, dsize=(720, 480), interpolation=cv2.INTER_AREA)
#     cap2.write(cap)

# cap2.release()




# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# cap = cv2.VideoCapture('tmp.h264')
# # cap = cv2.VideoCapture('results/dfbDAU.avi')
# cnt = 0
# while True:
#     print(cnt, end='\r')
#     cnt += 1
#     retval, frame = cap.read()
#     # cv2.imshow(f"{cnt}", frame)
#     # cv2.waitKey()
#     if not(retval):
#         print("end")
#         break
#     cv2.imwrite(f'./tmp/manual/{cnt}.jpg', frame)





# cap2.release()

# fileName = "dehazing"
# cap = cv2.VideoCapture(fileName+".mp4")
# retval, frame = cap.read()
# cv2.imwrite(fileName+".jpg", frame)


# print(vc.get(cv2.CAP_PROP_FRAME_COUNT))
# print(vc.get(cv2.CAP_PROP_FPS))
# print(vc.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(vc.get(cv2.CAP_PROP_FRAME_HEIGHT))