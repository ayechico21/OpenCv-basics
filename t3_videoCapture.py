import numpy as np
import cv2

# to capture feed from cam
# 0 identifies primary camera if there are multiple cameras
# second argument is optional, it is used to specify the api for video  capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#keep taking feed untill interrupted
while True:
    # ret: flags if capture was succesful {True,False}
    # frame: numpy array  which stores the feed {Each frame of video capture}
    ret, frame = cap.read()

    if not ret:
        print("Camera is Busy")
        break

    cv2.imshow('Feed', frame)

    # waits for keyboard input for 1ms, breaks out of loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release() # release camera
cv2.destroyAllWindows()

'''
Mirroring feed
'''

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera is Busy")
        break
    # cap has 17 objects, each represented by a int
    # 4 represents height
    # 3 represents width
    height = int(cap.get(4))
    width = int(cap.get(3))

    # Creating an black image of shape same as feed which acts as a canvas to mirror feed multiple times
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=.5, fy=.5)

    image[:height // 2, :width // 2] = smaller_frame  # Top left
    image[:height // 2, width // 2:] = smaller_frame  # Top right
    image[height // 2:, :width // 2] = smaller_frame  # Bottom left
    image[height // 2:, width // 2:] = smaller_frame  # Bottom right

    cv2.imshow('Feed', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
