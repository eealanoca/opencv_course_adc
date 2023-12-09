#videocaptura 

#importamos lib
import cv2

#creamos la videocaptura
cap=cv2.VideoCapture(0)

#crear el ciclo

while True:
    ret, frame = cap.read()

    print(ret)

    #mostrar los frames
    cv2.imshow("videocaptura", frame)

    t = cv2.waitKey(1)
    if t==27:
        break

cap.release()
cv2.destroyAllWindows()