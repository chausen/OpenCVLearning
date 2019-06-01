import cv2
import numpy as np
im = cv2.imread('c:/users/chausen/pictures/Camera Roll/red.jpg')

gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# raw = cv2.ctvColor(im, cv2.COLOR_BGR2HSV)
contours,h = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

final = np.zeros(im.shape,np.uint8)
mask = np.zeros(gray.shape,np.uint8)

for i in range(0,len(contours)):
    mask[...]=0
    cv2.drawContours(mask,contours,i,255,-1)
    cv2.drawContours(final,contours,i,cv2.mean(im,mask),-1)

cv2.imshow('im',im)
cv2.imshow('final',final)
cv2.waitKey(0)