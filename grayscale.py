from PIL import Image
from pylab import *

# functions

def display_img(img):
    img.show()

def display_negative_img(img):
    negative_img = Image.fromarray(255 - array(img))
    negative_img.show()

def display_clamp_img(img, start = 0, end = 255):
    gray_img_arr = ((float(end - start) / 255) * array(img) + start).astype(np.uint8)
    clamp_img = Image.fromarray(gray_img_arr)
    clamp_img.show()

def display_dark_img(img, deg):
    dark_img_arr = (255.0 * (array(img) / 255.0) ** deg).astype(np.uint8)
    dark_img = Image.fromarray(dark_img_arr)
    dark_img.show()

# work

img = Image.open('greece.jpg')

display_img(img)
display_negative_img(img)
display_clamp_img(img, 100, 200)
display_dark_img(img, 2)
