# Import libraries
import cv2
import numpy as np

# Corner detector parameters
corner_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)

# Execution modes
# 0 --> 48: Show video in real-time
# 1 --> 49: Blur filter
# 2 --> 50: Corner detector filter
# 3 --> 51: Edge filter

# Set the execution mode
mode = 48

# Video capture
cap = cv2.VideoCapture(0)

# Main loop
while True:
    ret, frame = cap.read()

    # Decide the processing mode

    # Normal mode
    if mode == 48:
        res = frame

    # Blur filter mode
    elif mode == 49:
        res = cv2.blur(frame, (135, 150))

    # Edge filter mode
    elif mode == 51:
        kernel = np.ones((5, 5))
        edge = cv2.Canny(cv2.GaussianBlur(frame, (13, 13), 0), 135, 150)
        res = cv2.dilate(edge, kernel, iterations=2)

    # Corner detector mode
    elif mode == 50:
        res = frame
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Calculate corners
        corners = cv2.goodFeaturesToTrack(gray, **corner_params)

        if corners is not None:
            for x, y in np.float32(corners).reshape(-1, 2):
                # Cast x, y values to integers
                x, y = int(x), int(y)
                # Draw detection circle
                cv2.circle(res, (x, y), 10, (255, 0, 0), 1)

    # Invalid mode
    elif mode != 48 or mode != 49 or mode != 50 or mode != 51:
        res = frame
        print("Invalid mode")

    cv2.imshow("video", res)

    t = cv2.waitKey(1)
    if t == 27:
        break
    elif t != -1:
        mode = t

cap.release()
cv2.destroyAllWindows()