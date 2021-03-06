import numpy as np
import cv2
import pickle

face_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade=cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')

recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
labels={"person_name":1}
with open("labell.pkl",'rb') as f:

    olabels=pickle.load(f)
    labels={v:k for k,v in olabels.items()}
cap=cv2.VideoCapture(0)

while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for (x,y,h,w) in faces:
        #print(x,y,h,w)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        id_,conf=recognizer.predict(roi_gray)

        if conf>=45:
            # and conf<=85:
            #print(id_)
            text=labels[id_]
            color={255,255,255}
            stroke=2
            cv2.putText(frame,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2,cv2.LINE_AA)
        img_item="my.png"
        cv2.imwrite(img_item,roi_color)

        color={255,0,0}
        stroke=2
        width=x+w
        height=y+h
        cv2.rectangle(frame,(x,y),(width,height),(255,0,0),2)
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
       
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cap.release()
cv2.waitKey(1500)
cv2.destroyAllWindows()