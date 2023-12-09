import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Translation transformation
im = cv2.imread('homeworks/homeworks_3/libro1.jpeg')
width = int(im.shape[1] / 5)
height = int(im.shape[0] / 5)
im = cv2.resize(im, (width, height), interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Key points
    num_keypoints = 500
    orb = cv2.ORB_create(num_keypoints)

    keypoints_im, descriptors_im = orb.detectAndCompute(gray_im, None)
    keypoints_frame, descriptors_frame = orb.detectAndCompute(gray_frame, None)

    im_display = cv2.drawKeypoints(im, keypoints_im, outImage=np.array([]), color=(255, 0, 0),
                                   flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    frame_display = cv2.drawKeypoints(frame, keypoints_frame, outImage=np.array([]), color=(255, 0, 0),
                                      flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors_im, descriptors_frame)
    matches = sorted(matches, key=lambda x: x.distance, reverse=False)

    good_matches = int(len(matches) * 0.1)
    matches = matches[:good_matches]

    img_matches = cv2.drawMatches(im, keypoints_im, frame, keypoints_frame, matches, None)

    points_im = np.zeros((len(matches), 2), dtype=np.float32)
    points_frame = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points_im[i, :] = keypoints_im[match.queryIdx].pt
        points_frame[i, :] = keypoints_frame[match.trainIdx].pt

    homography, mask = cv2.findHomography(points_frame, points_im, cv2.RANSAC)

    im_height, im_width, im_channels = im.shape
    img_perspective = cv2.warpPerspective(frame, homography, (im_width, im_height))

    # cv2.imshow("video capture", frame_display)
    # cv2.imshow("image", im_display)
    # cv2.imshow("matches", img_matches)
    cv2.imshow("matches", img_perspective)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
