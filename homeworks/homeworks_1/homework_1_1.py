# Homework_1_1: Given an image, crop something prominent from that image.

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Create the main matrix
img = 100 * np.ones((10, 10, 3), np.uint8)

# Modify the pixels to be extracted
img[4, 5, 0] = 255
img[4, 4, 0] = 0
img[5, 4, 0] = 255
img[5, 5, 0] = 0

img[4, 5, 1] = 0
img[4, 4, 1] = 255
img[5, 4, 1] = 0
img[5, 5, 1] = 255

img[4, 5, 2] = 255
img[4, 4, 2] = 255
img[5, 4, 2] = 0
img[5, 5, 2] = 0

# Show the channels
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(img)
ax1.set_title("IMAGE")

# Perform cropping (rows, columns)
crop = img[3:6, 3:7]

# Crop
ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(crop)
ax2.set_title("CROP")

plt.show()

# Now with images
# Read the image
image = cv2.imread('homeworks/homeworks_1/starman.png')

# Crop the region of interest
crop = image[239:418, 385:652]

# Show the crop
cv2.imshow('ORIGINAL IMAGE', image)
cv2.imshow('CROP', crop)

cv2.waitKey(0)
cv2.destroyAllWindows()

