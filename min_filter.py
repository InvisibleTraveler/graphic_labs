import scipy.misc
import scipy.ndimage

from PIL import Image

# functions

def display_min_filter_img(img, size):
    min_img_arr = scipy.ndimage.filters.minimum_filter(img, size = size, footprint = None, output = None, mode = 'reflect', cval = 0.0, origin = 0)
    min_img = Image.fromarray(min_img_arr)
    min_img.show()

# work

img = Image.open('greece.jpg')

img.show()
display_min_filter_img(img, 3)