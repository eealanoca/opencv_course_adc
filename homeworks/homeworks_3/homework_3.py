# Homework_3: Transformation that can be used to extract important points.

import numpy as np
import cv2

# Load image
im = cv2.imread('homeworks/homeworks_3/photo_2023-12-07_20-19-53.jpg')
width = int(im.shape[1] / 5)
height = int(im.shape[0] / 5)
im = cv2.resize(im, (width, height), interpolation=cv2.INTER_AREA)

# Convert image to grayscale
gray1 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Create ORB detector
num = 500
orb = cv2.ORB_create(num)

# Detect keypoints and compute descriptors for the reference image
keypoint1, descriptor1 = orb.detectAndCompute(gray1, None)

# Create a BFMatcher object
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert the video frame to grayscale
    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect keypoints and compute descriptors for the video frame
    keypoint2, descriptor2 = orb.detectAndCompute(gray2, None)

    # Match descriptors using the BFMatcher
    matches = matcher.match(descriptor1, descriptor2)

    # Sort them in ascending order of distance
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw only the first 10% of matches (you can adjust this ratio)
    good_matches = int(len(matches) * 0.1)
    matches = matches[:good_matches]

    # Draw keypoints on the video frame
    frame_display = cv2.drawKeypoints(frame, keypoint2, outImage=np.array([]), color=(0, 255, 0),
                                      flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    # Draw matches between the reference image and the video frame
    img_matches = cv2.drawMatches(im, keypoint1, frame, keypoint2, matches, None,
                                  flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

    # Display the modified frames
    cv2.imshow("Video Capture", frame_display)
    cv2.imshow("Matches", img_matches)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
