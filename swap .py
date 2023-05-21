import cv2
import numpy as np
img1 = cv2.imread('ggirl.jpg')
img2 = cv2.imread('girll.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces1 = face_cascade.detectMultiScale(gray1, 1.3, 5)
faces2 = face_cascade.detectMultiScale(gray2, 1.3, 5)
for (x1, y1, w1, h1) in faces1:
    for (x2, y2, w2, h2) in faces2:
        face1 = cv2.resize(img1[y1:y1+h1, x1:x1+w1], (w2, h2))
        face2 = cv2.resize(img2[y2:y2+h2, x2:x2+w2], (w1, h1))
        img1[y1:y1+h1, x1:x1+w1]=face2
        img2[y2:y2+h2, x2:x2+w2]=face1
cv2.imshow('swapped1.jpg', img1)
cv2.imshow('swapped2.jpg', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
