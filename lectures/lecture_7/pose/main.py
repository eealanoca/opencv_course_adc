import cv2

model='pose_deploy_linevec_faster_4_stages.prototxt'
pesos='pose_iter_160000.caffemodel'

numpuntos=15
pares=[ [0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8],[8,9], [9,10], [14,11], [11,12], [12,13] ]

net=cv2.dnn.readNetFromCaffe(model, pesos)

cap=cv2.VideoCapture(0)

p=False
e=False

while True:
    ret, frame=cap.read()

    rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    anchoframe=frame.shape[1]
    altoframe=frame.shape[0]

    tamnet=(368, 368)

    blob=cv2.dnn.blobFromImage(rgb, 1.0/255, tamnet, (0,0,0), swapRB=True, crop= False)

    net.setInput(blob)

    output=net.forward()

    scalex=anchoframe/output.shape[3]
    scaley=altoframe/output.shape[2]

    punt=[]

    umbral=0.1

    for i in range(numpuntos):
        probmap=output[0,i,:,:]

        minval, prob, minloc, puntos = cv2.minMaxLoc(probmap)

        x=scalex*puntos[0]
        y = scaley * puntos[1]

        if prob > umbral:
            punt.append((int(x), int(y)))
        else:
            punt.append(None)
    print(p,e)

    if p==True:
        for i, pu, in enumerate(punt):
            cv2.circle(frame, pu, 8, (255,0,255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frame, "{}".format(i), pu, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, lineType=cv2.LINE_AA)

    if e==True:

        for par in pares:
            parteA=par[0]
            parteB=par[1]

            if punt[parteA] and punt[parteB]:
                cv2.line(frame, punt[parteA], punt[parteB], (0,255,255), 2)
                cv2.circle(frame, punt[parteA], 8, (255,0,0), thickness=-1, lineType=cv2.FILLED)


    cv2.imshow("videocap", frame)

    t=cv2.waitKey(1)
    if t==27:
        break

    if t==112 or t==80:
        p=True
        e=False

    if t==101 or t==69:
        p=False
        e=True

cap.release()
cv2.destroyAllWindows()


