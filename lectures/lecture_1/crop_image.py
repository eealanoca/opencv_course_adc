#%% Import libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

#%% Create image
# Create the main matrix
img = 100 * np.ones((10, 10, 3), np.uint8)
img2 = 100 * np.ones((10, 10, 3), np.uint8)

#%% Modify the pixels to be extracted
# Modify the pixel (4,5) of the R matrix
img[4, 5, 0] = 255
img[4, 4, 0] = 0
img[5, 4, 0] = 255
img[5, 5, 0] = 0

# Modify the pixel (4,5) of the G matrix
img[4, 5, 1] = 0
img[4, 4, 1] = 255
img[5, 4, 1] = 0
img[5, 5, 1] = 255

# Modify the pixel (4,5) of the B matrix
img[4, 5, 2] = 255
img[4, 4, 2] = 255
img[5, 4, 2] = 0
img[5, 5, 2] = 0

# Perform cropping (rows, columns)
# crop = img[3:6, 3:7]
#
# # Show the channels
# fig = plt.figure()
# # Original image
# ax1 = fig.add_subplot(1, 2, 1)
# ax1.imshow(img)
# ax1.set_title("IMAGE")
#
# # Crop
# ax2 = fig.add_subplot(1, 2, 2)
# ax2.imshow(crop)
# ax2.set_title("CROP")
#
# plt.show()
#
# # Now with images
# # Read the image
image = cv2.imread('RDR.jpg')
#
# # Paint trick
crop = image[406:718, 669:951]

# Rows
# 406 row - 718
# 669 col - 951

# Show the crop
cv2.imshow('ORIGINAL IMAGE', image)
cv2.imshow('CROP', crop)

cv2.waitKey(0)