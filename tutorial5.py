import numpy as np
import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    height = int(cap.get(4))
    width = int(cap.get(3))

    # converting color scheme of feed from bgr to hsv
    # hsv: Hue Saturation Lightness/Brightness
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    '''
    To get hsv value of a bgr pixel
    bgr_color = np.array([255, 0, 0])
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
    '''
    # Upper & Lower bound of color range to be extracted from image
    # color are in hsv scheme
    lower = np.array([90, 50, 50])  # light blue shade hsv
    upper = np.array([130, 255, 255])  # dark blue shade hsv

    # creating a mask of the color range
    # mask is a portion of image
    mask = cv2.inRange(img, lower, upper)

    '''
    After mask is applied, only pixel matching the mask pixels are visible in the feed while
    all the other pixels are black (0 due to bitwise and b/w feed pixel & mask pixe)
    '''
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)  # original feed
    cv2.imshow('frame_hsv', img)  # feed with hsv color scheme
    cv2.imshow('mask', mask)  # mask
    cv2.imshow('Feed', result)  # feed after mask is applied

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
