import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def process_image(img):
    # Convert image to grayscale
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow('img', gray_img)
    # cv.waitKey(0)

    # Plot histogram
    # plt.hist(gray_img.flat, bins=256, range=(0, 255))
    # plt.show()
    # plt.switch_backend('TkAgg')
    hist = cv.calcHist([gray_img], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.show()
    # Apply CLAHE
    # clahe = cv.createCLAHE(clipLimit=10.0, tileGridSize=(2, 2))
    # enhanced_img = clahe.apply(gray_img) + 5

    # cv.imshow('img2', enhanced_img)
    cv.waitKey(0)

def main():
    imgage1 = cv.imread("cctv1.JPG")
    imgage2 = cv.imread("cctv2.JPG")
    imgage3 = cv.imread("cctv3.JPG")
    imgage4 = cv.imread("cctv4.JPG")

    num = int(input("Enter an integer corresponding to the image you want to process: "))

    if num == 1:
        process_image(imgage1)
    elif num == 2:
        process_image(imgage2)
    elif num == 3:
        process_image(imgage3)
    elif num == 4:
        process_image(imgage4)
    else:
        print("Invalid input! Enter an integer between 1 and 4.")

if __name__ == "__main__":
    main()
