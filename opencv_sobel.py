import cv2
import numpy as np 
from matplotlib import pyplot as plt 

# functions

def display_sobel_x(img, size):
    x_img = cv2.Sobel(img, -1, 1, 0, ksize = size)
    plt.imshow(x_img)
    plt.show()

def display_sobel_y(img, size):
    y_img = cv2.Sobel(img, -1, 0, 1, ksize = size)
    plt.imshow(y_img)
    plt.show()

# work

img = cv2.imread('greece.jpg')

display_sobel_x(img, 5)
display_sobel_y(img, 5)