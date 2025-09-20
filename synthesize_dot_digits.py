import cv2 as cv
import numpy as np


def solve(num, image):
    radius = 25 #radius of every colored dot
    matrix = np.array([
        #Every Row here Represents Numbers From 0 to 9 , with one reptesenting colored dot
        [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]], 
        [[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
        [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    ])
    for i in range(len(num)):
        number = int(num[i])
        for row in range(5):
            for col in range(len(matrix[number][row])):
                #(55,55) is the initial coordinate
                x = i * (200) + col * (55) + 55
                y = row * (55) + 55
                #if it is colored dot then we create that circle on our image using cv.circle
                if matrix[number][row][col]== 1:
                    cv.circle(image, (x, y),
                              25, (255),
                              thickness=cv.FILLED)
    

#Please Note that the inital coordinates and other coordinates are obtained by hit and trial 

num = str(input('Please enter any number having more than 2 digits :'))
num = num[-2:]
#Creating a blank black image of required dimensions
img = np.zeros((300, 500), dtype='uint8')
solve(num, img)
cv.imshow('vbf', img)
cv.waitKey(0)