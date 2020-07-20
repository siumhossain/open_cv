import cv2
import numpy as np 

img = cv2.imread('cr7.jpg')

equ = cv2.equalizeHist(img)

res = np.hstack((img,equ)) #stacking images side-by-side


cv2.imwrite('res.jpg',res)

