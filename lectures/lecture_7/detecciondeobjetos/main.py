import cv2

model= 'frozen_inference_graph.pb'
config='ssd_mobilenet_v2_coco_2018_03_29.pbtxt'
clases='coco_labels.txt'

with open(clases) as cl:
    labels=cl.read().split("\n")
print(labels)

net=cv2.dnn.readNetFromTensorflow(model, config)

def object_detected(net, img):

    dim=300

    #preprocesamiento de las imagenes
    blob=cv2.dnn.blobFromImage(img, 1.0, size=(dim, dim), mean=(0,0,0), swapRB=True, crop=False)

    net.setInput(blob)

    objetos = net.forward()

    return objetos

def text(img, text, x,y):
    sizetext=cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 1)

    dim=sizetext[0]
    baseline=sizetext[1]

    cv2.rectangle(img, (x, y-dim[1]-baseline), (x+dim[0], y+baseline), (0,0,0), cv2.FILLED )

    cv2.putText(img, text, (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 1)

def dibujar_obj(img, objects, umbral=0.5):

    filas=img.shape[0]
    column=img.shape[1]

    for i in range(objects.shape[2]):
        clase = int(objects[0,0,i,1])
        puntaje = float(objects[0, 0, i, 2])

        x=int(objects[0,0,i,3]*column)
        y = int(objects[0, 0, i, 4] * filas)
        w = int(objects[0, 0, i, 5] * column-x)
        h = int(objects[0, 0, i, 6] * filas-x)

        if puntaje > umbral:
            text(img, "{}".format(labels[clase]), x,y)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,225,0), 2)

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:
    ret, frame=cap.read()

    detect=object_detected(net, frame)

    dibujar_obj(frame,detect)

    cv2.imshow("videocaptura", frame)

    t=cv2.waitKey(1)
    if t==27:
        break

cap.release()
cv2.destroyAllWindows()