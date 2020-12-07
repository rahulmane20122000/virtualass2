from cv2 import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)

while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in face:
        # print(x,y,w,h)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

        cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27:
       break
cam.release()
cv2.destroyAllWindows()

