import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read images
# Read in grayscale
img_gray = cv2.imread("RDR.jpg", 0)  # 1 CHANNEL 1 MATRIX

# Read in color
img_rgb = cv2.imread("RDR.jpg", 1)  # 3 CHANNELS 3 MATRICES

# Read
img = cv2.imread("RDR.jpg")  # 3 CHANNELS 3 MATRICES

# Extract main attributes
size_gray = img_gray.shape
dtype_gray = img_gray.dtype
print("Gray Size | Data Type |", size_gray, dtype_gray)

# Extract main attributes
size_rgb = img_rgb.shape
dtype_rgb = img_rgb.dtype
print("RGB Size | Data Type |", size_rgb, dtype_rgb)

# Show the images
# cv2.imshow("GRAY", img_gray)
# cv2.imshow("RGB", img_rgb)
# cv2.imshow("IMG", img)

# Correct COLOR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show our image
plt.imshow(img)
plt.show()

# Wait for key press to close the windows
cv2.waitKey(0)