# importing opencv
import cv2

#reading an image
import cv2

img = cv2.imread('assets\\wallpaper.png', 1)
'''
-1: Default, transparency of image will be neglected
0 : Load image in greyscale
1 : Load image as it is
'''

cv2.imshow('Image', img)  # to view an image
cv2.waitKey(0)  # waits till any key is pressed
# cv2.waitKey(5)  # waits 5 milisec
cv2.destroyAllWindows()  # destroy all windows so no window maybe running in background

img2 = cv2.resize(img, (800, 800))  # resize image to 800 X 800
cv2.imshow('Image', img2)
cv2.waitKey(2000)  # waits for 2 sec
cv2.destroyAllWindows()

img3 = cv2.resize(img, (0, 0), fx=.5,fy=.5)  # resize image to  half width & height
cv2.imshow('Image', img3)
cv2.waitKey(2000)
cv2.destroyAllWindows()

img4 = cv2.rotate(img3, cv2.ROTATE_90_CLOCKWISE)  # rotate an image
cv2.imshow('Image', img4)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# save the manipulated image
cv2.imwrite('assets\\new_wallpaper.png', img4)