import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Transformation by translation
im = cv2.imread('homeworks/homeworks_3/libro1.jpeg')
width = int(im.shape[1] / 5)
height = int(im.shape[0] / 5)
im = cv2.resize(im, (width, height), interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap.read()

    gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Key points
    num = 500
    orb = cv2.ORB_create(num)

    keypoint1, descriptor1 = orb.detectAndCompute(gray2, None)
    keypoint2, descriptor2 = orb.detectAndCompute(gray1, None)

    im_display = cv2.drawKeypoints(im, keypoint1, outImage=np.array([]), color=(255, 0, 0),
                                   flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    frame_display = cv2.drawKeypoints(frame, keypoint2, outImage=np.array([]), color=(255, 0, 0),
                                      flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptor1, descriptor2)
    matches = sorted(matches, key=lambda x: x.distance, reverse=False)

    good_matches = int(len(matches) * 0.1)
    matches = matches[:good_matches]

    img_matches = cv2.drawMatches(im, keypoint1, frame, keypoint2, matches, None)

    cv2.imshow("Video Capture", frame_display)
    cv2.imshow("Image", im_display)
    cv2.imshow("Matches", img_matches)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()