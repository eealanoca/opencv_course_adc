# Homework_2: Create your own filter.

import cv2

# Create video capture object
cap = cv2.VideoCapture(0)
# Change the camera index number as needed

# Main loop
while True:
    # Read frames from video capture
    ret, frame = cap.read()

    # Convert frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Alternatively, you can use LUV color space
    # luv_frame = cv2.cvtColor(frame, cv2.COLOR_LUV2BGR)
    # Or convert back to BGR from HSV color space
    # bgr_frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

    # Print the return value
    print(ret)

    # Display the converted frame
    cv2.imshow("Converted Frame", hsv_frame)
    # Alternatively, you can use the other frames
    # cv2.imshow("Converted Frame", luv_frame)
    # cv2.imshow("Converted Frame", bgr_frame)

    # Wait for key press
    key = cv2.waitKey(1)
    if key == 27:  # If ESC key is pressed, exit the loop
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
