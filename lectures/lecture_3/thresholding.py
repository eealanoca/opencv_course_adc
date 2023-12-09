# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('maquina.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a matrix of ones with the same shape as grayscale image
matrix = np.ones(gray.shape, dtype='uint8') * 50

# Increase image brightness
brightened = cv2.add(gray, matrix)

# Thresholding
_, img_thresh1 = cv2.threshold(brightened, 160, 255, cv2.THRESH_BINARY)
_, img_thresh2 = cv2.threshold(brightened, 180, 255, cv2.THRESH_BINARY_INV)

# Adaptive thresholding
img_adaptive1 = cv2.adaptiveThreshold(brightened, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# Decrease brightness
darkened = cv2.subtract(gray, matrix)

# Threshold without brightness
_, img_thresh3 = cv2.threshold(darkened, 50, 255, cv2.THRESH_BINARY)
_, img_thresh4 = cv2.threshold(darkened, 80, 255, cv2.THRESH_BINARY_INV)

# Adaptive thresholding for darkened image
img_adaptive2 = cv2.adaptiveThreshold(darkened, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# Display images
fig = plt.figure()

# Brightened images
fg1 = fig.add_subplot(2, 4, 1)
fg1.imshow(brightened, cmap="gray")
fg1.set_title("Brightened Image")

fg2 = fig.add_subplot(2, 4, 2)
fg2.imshow(img_thresh1, cmap="gray")
fg2.set_title("Thresholding 1")

fg3 = fig.add_subplot(2, 4, 3)
fg3.imshow(img_thresh2, cmap="gray")
fg3.set_title("Thresholding 2")

fg4 = fig.add_subplot(2, 4, 4)
fg4.imshow(img_adaptive1, cmap="gray")
fg4.set_title("Adaptive Thresholding 1")

# Darkened images
fg5 = fig.add_subplot(2, 4, 5)
fg5.imshow(darkened, cmap="gray")
fg5.set_title("Darkened Image")

fg6 = fig.add_subplot(2, 4, 6)
fg6.imshow(img_thresh3, cmap="gray")
fg6.set_title("Thresholding Dark 1")

fg7 = fig.add_subplot(2, 4, 7)
fg7.imshow(img_thresh4, cmap="gray")
fg7.set_title("Thresholding Dark 2")

fg8 = fig.add_subplot(2, 4, 8)
fg8.imshow(img_adaptive2, cmap="gray")
fg8.set_title("Adaptive Thresholding Dark")

plt.show()
