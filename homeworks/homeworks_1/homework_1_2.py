# Homework_1_2: Given an image, resize it in any way you prefer.
# Import libraries
import cv2

# Read the image
img = cv2.imread('homeworks/homeworks_1/starman.png')

# Different types of resizing
resized1 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
resized2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
resized3 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# Custom resizing
width = 600 
height = 800  
size = (width, height)
resized_custom = cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)

# Display the resized images
cv2.imshow('Resized1', resized1)
cv2.imshow('Resized2', resized2)
cv2.imshow('Resized3', resized3)
cv2.imshow('Resized Custom', resized_custom)

cv2.waitKey(0)
