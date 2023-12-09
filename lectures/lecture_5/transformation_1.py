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

    cv2.imshow("Video Capture", frame_display)
    cv2.imshow("Image", im_display)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()