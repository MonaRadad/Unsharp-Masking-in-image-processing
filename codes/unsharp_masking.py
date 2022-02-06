# -*- coding: utf-8 -*-
"""Unsharp-Masking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o4c5DLVsaO04CeWQJeJ349pd6rFosloz
"""

!apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python
import cv2
from PIL import Image
from google.colab.patches import cv2_imshow

import numpy as np
import pandas as pd
import cv2

gussian_3x3 = np.array([[1,2,1],
                        [2,4,2],
                        [1,2,1]
                        ])/16


def gussian_filter(image,kernel):
    
    n = kernel.shape[0]
    G = np.zeros((image.shape[0],image.shape[1]))

    for i in range(image.shape[0]):
      if image.shape[0] - i < n:
        break
      for j in range(image.shape[1]):
        if image.shape[1] - j < n:
          break
        G[i][j] = (kernel * image[i:i+n,j:j+n]).sum()

    return G


# 4
child = cv2.imread("child.jpg")
child = cv2.cvtColor(child,cv2.COLOR_BGR2GRAY)

def mean_filter(image,n):

  mean_filter = np.ones((n,n))/(n*n)
  G = np.zeros((image.shape[0],image.shape[1]))

  for i in range(image.shape[0]):
    if image.shape[0] - i < n:
      break
    for j in range(image.shape[1]):
      if image.shape[1] - j < n:
        break
      G[i][j] = (mean_filter * image[i:i+n,j:j+n]).sum()

  
  return G 

child_unsharp = mean_filter(child,3)
unsharp_mask = child - child_unsharp
result1 = child + unsharp_mask
cv2_imshow(result1)


child_unsharp_gussian = gussian_filter(child,gussian_3x3)
unsharp_mask_gussian = child - child_unsharp_gussian
result2 = child + unsharp_mask_gussian
cv2_imshow(result2)


child_unsharp = mean_filter(child,5)
unsharp_mask = child - child_unsharp
result3 = child + unsharp_mask
cv2_imshow(result3)


child_unsharp = mean_filter(child,7)
unsharp_mask = child - child_unsharp
result5 = child + unsharp_mask
cv2_imshow(result5)


child_unsharp = mean_filter(child,9)
unsharp_mask = child - child_unsharp
result9 = child + unsharp_mask
cv2_imshow(result9)

def median_filter(image):

  
  G = np.zeros((image.shape[0],image.shape[1]))
  temp = np.zeros((3,3))
  for i in range(image.shape[0]):
    if image.shape[0] - i < 3:
      break
    for j in range(image.shape[1]):
      if image.shape[1] - j < 3:
        break
      temp = image[i:i+3,j:j+3]
      G[i][j] = np.median(temp)

  
  return G 

# static gussian filter

kernel = np.array([[-1,-2, -1],[-2, 12, -2],[-1,-2,-1]])/16
derivative = gussian_filter(child,kernel)

res = derivative+child
cv2_imshow(res)

# dynamic gaussian filter

kernel1 = np.array([[0,0, 0],[-2, 2, 0],[0,0,0]])
derivative1 = gussian_filter(child,kernel1)/16
print(derivative1.sum())

kernel2 = np.array([[-1,0, 0],[0, 1, 0],[0,0,0]])
derivative2 = gussian_filter(child,kernel2)
print(derivative2.sum())


# lower than threshold
# kernel3 = np.array([[0,-2, 0],[0, 2, 0],[0,0,0]])
# derivative3 = gussian_filter(child,kernel3)
# print(derivative3.sum())

# lower than threshold
# kernel4 = np.array([[0,0, -1],[0, 1, 0],[0,0,0]])
# derivative4 = gussian_filter(child,kernel4)
# print(derivative4.sum())

# lower than threshold
# kernel5 = np.array([[0,0, 0],[0, 2, -2],[0,0,0]])
# derivative5 = gussian_filter(child,kernel5)
# print(derivative5.sum())


# lower than threshold
# kernel6 = np.array([[0,0, 0],[0, 1, 0],[0,0,-1]])
# derivative6 = gussian_filter(child,kernel6)
# print(derivative6.sum())

kernel7 = np.array([[0,0, 0],[0, 2, 0],[0,-2,0]])
derivative7 = gussian_filter(child,kernel7)
print(derivative7.sum())

kernel8 = np.array([[0,0, 0],[0, 1, 0],[-1,0,0]])
derivative8 = gussian_filter(child,kernel8)
print(derivative8.sum())

cv2_imshow(derivative1+derivative2+derivative7+derivative8+child)