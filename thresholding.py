
import cv2 as cv
import numpy as np

def remove_gutter_shadows(image):
    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    th = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 27, 11)
    cv.imshow('Thresholded Image', th)
    cv.waitKey(0)
    cv.destroyAllWindows()


img1 = cv.imread("gutters1.jpg")
img2 = cv.imread("gutters2.jpg")
img3 = cv.imread("gutters3.jpg")

num = input("Enter an integer corresponding to the image you want to remove shadows from gutters: ")

if num == '1':
    remove_gutter_shadows(img1)
elif num == '2':
    remove_gutter_shadows(img2)
elif num == '3':
    remove_gutter_shadows(img3)
else:
    print("Invalid Input! Please enter a number between 1 and 3.")