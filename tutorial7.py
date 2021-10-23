import numpy as np
import cv2

img = cv2.imread('assests\\soccer.jpg', 0)
img = cv2.resize(img, (0, 0), fx=.7, fy=.7)
template = cv2.imread('assests\\ball.png', 0)
template = cv2.resize(template, (0, 0), fx=.7, fy=.7)
height, width = template.shape

# various methods in opencv for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    # matching image with template via convolution of template array over image array
    result = cv2.matchTemplate(img2, template, method)
    '''
    In convolution, matching block gives higher value than other blocks
    img (H,W)
    temp(h,w)
    result(H-h+1,W-w+1) 
    '''
    # get min & max value and their location in img
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:  # these two method take min_val
        top_left = min_loc  # top left corner of matching block
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + width, top_left[1] + height)  # finding other corner of rectangle
    # since matching block will be of size of template

    cv2.rectangle(img2, top_left, bottom_right, 255, 5)  # rectangle around matching block
    cv2.imshow('match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
