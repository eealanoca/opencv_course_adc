import cv2

# Create video capture object
cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))

print(width, height)

# Create video writer object
out = cv2.VideoWriter('video2.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 40, (width, height))

# Video processing loop
while True:
    ret, frame = cap.read()

    # Write frame to video file
    out.write(frame)

    # Display frames
    cv2.imshow("Video Capture", frame)

    # Exit loop on 'Esc' key press
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release video capture and destroy windows
cap.release()
cv2.destroyAllWindows()