import dlib
import cv2
import get_points

cap = cv2.VideoCapture(0)

print('Pulsa P para pausar el video y empezar el seguimiento')

def tracker(img, puntos):

    tracker = dlib.correlation_tracker()

    tracker.start_track(img, dlib.rectangle(*points[0]))
    while True:

        ret, img = cap.read()
        if not ret:
            print("No se ejecuto la captura :(")
            exit()

        tracker.update(img)
        rect = tracker.get_position()
        pt1 = (int(rect.left()), int(rect.top()))
        pt2 = (int(rect.right()), int(rect.bottom()))
        cv2.rectangle(img, pt1, pt2, (255, 255, 255), 3)
        print("Objecto tracked en [{}, {}] \r".format(pt1, pt2), )
        loc = (int(rect.left()), int(rect.top() - 20))
        txt = "Objecto tracked en [{}, {}]".format(pt1, pt2)
        cv2.putText(img, txt, loc, cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 1)

        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) == 27:
            break


while True:

    ret, frame = cap.read()

    t = cv2.waitKey(1)

    if not ret:
        print('No se pudo capturar la camara')
        exit()

    frame = cv2.flip(frame, 1)

    if (t == ord('p')):
        points = get_points.run(frame)
        if not points:
            print("ERROR: No objeto para seguimiento.")
            exit()
        if points:
            tracker(img = frame, puntos = points)
        break

    cv2.imshow("IMAGEN", frame)


cv2.destroyAllWindows()