import cv2

# Read the image
image = cv2.imread('RDR.jpg')

# Rotate 1
rotation_1 = cv2.flip(image, 0)

# Rotate 2
rotation_2 = cv2.flip(image, 1)

# Rotate 3
rotation_3 = cv2.flip(image, -1)

# Show the original image
cv2.imshow('ORIGINAL IMAGE', image)

# Show rotation 1
cv2.imshow('ROTATION 1', rotation_1)

# Show rotation 2
cv2.imshow('ROTATION 2', rotation_2)

# Show rotation 3
cv2.imshow('ROTATION 3', rotation_3)

cv2.waitKey(0)