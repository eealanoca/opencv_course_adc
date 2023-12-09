import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read images
img = cv2.imread('maquina.png')
imgmat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create matrices
matriz = np.ones(gray.shape, dtype='uint8') * 50
matrizcolor = np.ones(img.shape, dtype='uint8') * 50

# Increase brightness
brillocolor = cv2.add(img, matrizcolor)
brillantecol = cv2.cvtColor(brillocolor, cv2.COLOR_BGR2RGB)

# Decrease brightness
oscurocolor = cv2.subtract(img, matrizcolor)
oscur = cv2.cvtColor(oscurocolor, cv2.COLOR_BGR2RGB)

# Increase brightness in grayscale
brillogris = cv2.add(gray, matriz)

# Decrease brightness in grayscale
oscurogris = cv2.subtract(gray, matriz)

# Display figures
fig = plt.figure()

# Original image
fg1 = fig.add_subplot(2, 3, 1)
fg1.imshow(imgmat)
fg1.set_title("Original Image")

# Brightness
fg2 = fig.add_subplot(2, 3, 2)
fg2.imshow(brillantecol)
fg2.set_title("Increased Brightness")

# Darkness
fg3 = fig.add_subplot(2, 3, 3)
fg3.imshow(oscur)
fg3.set_title("Decreased Brightness")

# Grayscale original
fg4 = fig.add_subplot(2, 3, 4)
fg4.imshow(gray, cmap="gray")
fg4.set_title("Grayscale Image")

# Brightness in grayscale
fg5 = fig.add_subplot(2, 3, 5)
fg5.imshow(brillogris, cmap="gray")
fg5.set_title("Increased Brightness in Grayscale")

# Darkness in grayscale
fg6 = fig.add_subplot(2, 3, 6)
fg6.imshow(oscurogris, cmap="gray")
fg6.set_title("Decreased Brightness in Grayscale")

plt.show()

cv2.imshow('Increased Brightness', brillantecol)
cv2.waitKey(0)