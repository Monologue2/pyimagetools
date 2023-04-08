import numpy as np
import cv2
import math
from heapq import heappush, heappop
import torch
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

  
# def PSNR(original, compressed):
#     mse = np.mean((original - compressed) ** 2)
#     if(mse == 0):  # MSE is zero means no noise is present in the signal .
#                   # Therefore PSNR have no importance.
#         return 100
#     max_pixel = 255.0
#     psnr = 20 * log10(max_pixel / sqrt(mse))
#     return psnr
# def psnr(ori_img, con_img):
#   """
  
#   @params ori_img: 원본 이미지
#   @params con_img: 비교 대상 이미지
#   """
  
#   # 해당 이미지의 최대값 (채널 최대값 - 최솟값)
#   max_pixel = 255.0

#   # MSE 계산
#   mse = np.mean((ori_img - con_img)**2)

#   if mse ==0:
#     return 100
  
#   # PSNR 계산
#   psnr = 20* math.log10(max_pixel / math.sqrt(mse))
  
#   return psnr
def calc_psnr(orig, pred):
  return 20. * torch.log10(255./torch.sqrt(torch.mean((orig - pred) ** 2)))
psnrs = []
ssims = []
for i in range(1, 501):
  s = f"{i}.jpg"
  img1 = cv2.imread('datas/aod/aod/'+s)
  img2 = cv2.imread('datas/aod/aod_manual/'+s)
  
  print(s, end="\r")
  psnrs.append(psnr(img1, img2))
  ssims.append(ssim(img1, img2, multichannel=True))

print("PSNR min: ", min(psnrs))
print("PSNR max: ", max(psnrs))
print("PSNR avg: ", sum(psnrs) / 500)

# print("SSIM min: ", min(ssims))
# print("SSIM max: ", max(ssims))
# print("SSIM avg: ", sum(ssims) / 500)
