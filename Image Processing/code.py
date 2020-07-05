import numpy as np
import cv2
face_cascade=cv2.CascadeClassifier("cascade.xml")
img=cv2.imread("picture.jpg",1)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
resized=cv2.resize(img,(600,500))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.imshow("pic",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()