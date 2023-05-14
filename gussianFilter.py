import cv2
import numpy as np

# Read the image
img = cv2.imread('noise3.jpg')

# Apply Gaussian blur with kernel size (x,y) and sigma value of x
gaussian = cv2.GaussianBlur(img, (3,3), 0)
gaussian2 = cv2.GaussianBlur(img, (9,9), 0)
gaussian3 = cv2.GaussianBlur(img, (21,21), 0)
gaussian4 = cv2.GaussianBlur(img, (3,3), 50)

# gaussian = cv2.GaussianBlur(img, (5,5), 0)
# gaussian2 = cv2.GaussianBlur(img, (5,5), 5)
# gaussian3 = cv2.GaussianBlur(img, (5,5), 25)
# gaussian4 = cv2.GaussianBlur(img, (5,5), 100)

# Display the original and Gaussian filtered image
cv2.imshow('Original', img)
cv2.imshow('Gaussian', gaussian)
cv2.imshow('Gaussian2', gaussian2)
cv2.imshow('Gaussian3', gaussian3)
cv2.imshow('Gaussian4', gaussian4)

cv2.waitKey(0)
cv2.destroyAllWindows()