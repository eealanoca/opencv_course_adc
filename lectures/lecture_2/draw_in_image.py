# Import libraries
import cv2

# Read image
img = cv2.imread('motor.jpg')

# Resize image
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# Draw a line
# variable = cv2.line(img, pt1(x,y), pt2(x,y), color, thickness, lineType)
img = cv2.line(img, (int(252/2), int(641/2)), (int(547/2), int(582/2)), (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

# Draw a circle
# variable = cv2.circle(img, center(x,y), radius, color, thickness, lineType)
img = cv2.circle(img, (int(657/2), int(552/2)), 50, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

# Draw a rectangle
# variable = cv2.rectangle(img, pt1(x,y), pt2(x,y), color, thickness, lineType)
img = cv2.rectangle(img, (int(417/2), int(426/2)), (int(549/2), int(549/2)), (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

# Add text
# variable = cv2.putText(img, text, org(x,y), fontFace, fontScale, color, thickness)
text = "gear detected"
font = cv2.FONT_ITALIC
font_scale = 1.1
color = (0, 255, 0)
thickness = 2
img = cv2.putText(img, text, (int(300/2), int(696/2)), font, font_scale, color, thickness)

# Display image
cv2.imshow('image', img)
cv2.waitKey(0)