import cv2

img = cv2.imread("assets\\wallpaper.png")
img = cv2.resize(img, (0, 0), fx=.5, fy=.5)
'''
Images are stored as numpy arrays
channels= RGB values
in opencv, it is BGR
'''
print(img.shape)  # (no. of rows, no. of columns, channels)
print(img[20][45])  # printing pixel at 20th row & 45th column [B,G,R]

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Changing pixel values
for i in range(50):
    for j in range(img.shape[1]):
        img[i][j] = [0, 0, 0]  # black
# top border in now black
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# loading a fresh image
img = cv2.imread("assets\wallpaper.png")
img = cv2.resize(img, (0, 0), fx=.5, fy=.5)

# Copying and pasting a part of image
tag = img[100:450, 500:750]
img[50:400, 1000:1250] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
