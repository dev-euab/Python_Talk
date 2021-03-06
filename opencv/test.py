import cv2 
import numpy as np #=> trabajar con matrices

cam = cv2.VideoCapture(0) # => invocacion de la camara web

kernel = np.ones((5,5),np.uint8) # => "Filtrar imagen"

while (True):
    ret, frame = cam.read()
    
    rangomax = np.array([50,255,50]) #azul verde rojo
    rangomin = np.array([0,51,0])

    mascara = cv2.inRange(frame,rangomin,rangomax)

    opening = cv2.morphologyEx(mascara , cv2.MORPH_OPEN,kernel)

    ##Dibujar el rentangulo

    x,y,w,h = cv2.boundingRect(opening)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.circle(frame,(x+w/2,y+h/2),5,(0,0,255),-1)
    cv2.imshow('camara',frame)
    k = cv2.waitKey(1) & 0xFF

    if k==27:
        break
    



