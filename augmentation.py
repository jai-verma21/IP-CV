import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("jigsaw.jpg")

sub_img1 = img[150:330, 515:700]
sub_img1 = cv.flip(sub_img1, 1)

img[150:330, 515:700] = sub_img1
# cv.imshow('dcjnd', img)
sub_img2 = img[370:420, 370:795]
sub_img2 = cv.flip(sub_img2, 0)
img[370:420, 370:795] = sub_img2
sub_img3 = img[0:200, 0:190]
b,g,r=cv.split(sub_img3)
sub_img3=cv.merge([g,b,r])

sub_img4 = img[200:410, 0:190]
sub_img4 = cv.flip(sub_img4, 0)

img[200:400, 0:190] = sub_img3
img[0:210, 0:190] = sub_img4
cv.imshow('dcjnd', img)
cv.waitKey(0)