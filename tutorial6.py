import numpy as np
import cv2
'''
Shi-Tomasi corner detector 
'''
img = cv2.imread('assests\chessboard.png')
img = cv2.resize(img, (0, 0), fx=.5, fy=.5)
cv2.imshow('img', img)
# Greyscale version of feed
# Easier to detect corners in grayscale image than hsv or bgr image
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# npArray of 100 best corners in the image
# .01 is confidence level of detected corner [0,1]
# 10 is the minimum euclidean distance b/w two corners in pixel to avoid overlapping of detected corners
corners = cv2.goodFeaturesToTrack(grey, 100, .01, 10)

corners = np.int0(corners)  # changing datatype of corners from float to int

# drawing circle at the detected corners
for corner in corners:
    x, y = corner.ravel()  # npArray flatten [[x,y]] -> [x,y]
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

cv2.imshow('circles', img)

# drawing lines from each corner to all the other corners
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        # cv2 func take tuple values as arguments
        corner1 = corners[i].ravel()
        corner2 = corners[j].ravel()

        # generate 3 random int b/w 0-255, map each value to int type
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()