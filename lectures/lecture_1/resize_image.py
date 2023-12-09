# Import libraries
import cv2

# Read the image
img = cv2.imread('RDR.jpg')

# Different types of resizing
resized1 = cv2.resize(img, None, fx=0.5, fy=0.5)
resized2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
resized3 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# Manual resizing
width = 300
height = 400
size = (width, height)
resized4 = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)

# Display the resized images
# cv2.imshow('Original', img)
# cv2.imshow('Resized2', resized2)
# cv2.imshow('Resized3', resized3)
cv2.imshow('Resized4', resized4)

cv2.waitKey(0)