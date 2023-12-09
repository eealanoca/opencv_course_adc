import cv2

# Create video capture object
cap = cv2.VideoCapture(0)

# Main loop
while True:
    # Read frames from video capture
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Print the return value
    print(ret)

    # Display the grayscale frame
    cv2.imshow("Gray Frame", gray_frame)

    # Wait for key press
    key = cv2.waitKey(1)
    if key == 27:  # If ESC key is pressed, exit the loop
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()