import cv2
import numpy as np 
import sys


def pHash(img_address):
    img=cv2.imread(img_address,cv2.IMREAD_GRAYSCALE)
    if img == "":
        return
    img=cv2.resize(img,(64,64),interpolation=cv2.INTER_CUBIC)
    h,w=img.shape[:2]
    vis0=np.zeros((h,w),np.float32)
    vis0[:h,:w]=img
    vis1=cv2.dct(cv2.dct(vis0))
    vis1.resize(16,16)
    img_list=np.ndarray.flatten(vis1)
    avg=sum(img_list)/len(img_list)
    avg_list=['0' if i<avg else '1' for i in img_list]
    return ''.join(['%x' % int(''.join(avg_list[x:x+4]),2) for x in range(0,256,4)])

# a=pHash(r"桌面\下载.jpg")
# b=pHash(r"C:\Users\26696\Desktop\car_img\dhc\dhc1.jpg")
# print(Levenshtein.distance(a,b))
