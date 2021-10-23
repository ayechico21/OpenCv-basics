import numpy as np
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
'''
Cartesian plane starts from top left in open cv
(0,0) denotes top left corner of screen
move down: increase height
move right : increase width
'''
while True:
    ret, frame = cap.read()
    height = int(cap.get(4))
    width = int(cap.get(3))

    # Draw a line on the feed from (0,0) to bottom left corner (width,height)
    # colour in BGR value (B,G,R)
    # 10 is the line weight
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)

    # Draw a rectangle from top left corner to bottom right corner eg.(100, 100) to (300, 300)
    # 5 denotes the edges width
    # -1 in edge width to fill the rectangle
    img = cv2.rectangle(img, (10, 100), (100, 200), (0, 0, 255), 5)
    img = cv2.rectangle(img, (10, 220), (100, 320), (0, 255, 0), -1)

    # Draw a circle from centre (500, 200)
    # 5 denotes the circle width
    # -1 in edge width to fill the circle
    img = cv2.circle(img, (500, 200), 100, (50, 100, 150),5)
    img = cv2.circle(img, (500, 200), 50, (150, 200, 50), -1)

    # font: font style for text eg. italics, hershey
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Write text on  the screen
    # 1.5 is the font size
    # 5 is the font weight
    img = cv2.putText(img, 'This is OpenCV', (200, 400), font, 1.5, (0, 0, 0), 5)

    cv2.imshow('Feed', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
