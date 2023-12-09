import cv2

cap=cv2.VideoCapture(0)

#modelo
red=cv2.dnn.readNetFromCaffe("opencv_face_detector.prototxt", "res10_300x300_ssd_iter_140000.caffemodel")

#parametros del modelo
anchonet=300
altonet=300
media=[104, 177, 123]
umbral=0.7

while True:
    ret, frame=cap.read()

    if not ret:
        break

    frame=cv2.flip(frame,1)

    altoframe=frame.shape[0]
    anchoframe=frame.shape[1]

    blob=cv2.dnn.blobFromImage(frame, 1.0, (anchonet, altonet), media, swapRB=False, crop= False)

    red.setInput(blob)
    deteccion=red.forward()

    for i in range(deteccion.shape[2]):
        conf=deteccion[0,0,i,2]
        if conf > umbral:
            xmin=int(deteccion[0,0,i,3]*anchoframe)
            ymin=int(deteccion[0,0,i,4]*altoframe)

            xmax = int(deteccion[0, 0, i, 5] * anchoframe)
            ymax = int(deteccion[0, 0, i, 6] * altoframe)

            cv2.rectangle(frame, (xmin, ymin),(xmax, ymax), (0,0,255), 2)
            label="confianza de deteccion: %.4f" %conf
            label_size, base_line=cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5,1)

            cv2.rectangle(frame, (xmin, ymin-label_size[1]),(xmin+label_size[0], ymin+base_line), (0,0,0), cv2.FILLED )

            cv2.putText(frame, label, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1)
    cv2.imshow("detector de objetos", frame)

    t=cv2.waitKey(1)
    if t==27:
        break
cv2.destroyAllWindows()
cap.release()

