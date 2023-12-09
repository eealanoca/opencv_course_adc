import cv2

red=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()

    if not ret:
        break
    frame = cv2.flip(frame,1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cara=red.detectMultiScale(gray, 1.1, 4)
    for(x,y,w,h) in cara:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,0,255),2)
    cv2.imshow("detector con cascade", frame)
    t = cv2.waitKey(1)
    if t == 27:
        break
cv2.destroyAllWindows()
cap.release()
