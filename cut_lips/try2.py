import cv2
import dlib
import numpy as np
from PIL import Image,ImageFilter

def createBox(img,points):
    bbox=cv2.boundingRect(points)
    x,y,w,h=bbox
    imgcrop=img[y:y+h,x:x+w]
    imgcrop=cv2.resize(imgcrop,(0,0),None,3,3)
    return imgcrop

def detect(img,i):
    

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector(img_gray)

    for face in faces:
        landmarks=predictor(img_gray,face)
        myPoints=[]
        for n in range(48,68):
            x=landmarks.part(n).x
            y=landmarks.part(n).y
            if(x>landmarks.part(61).x):
                myPoints.append([x+15,y+7])
            else:
                myPoints.append([x-15,y-7])
        myPoints=np.array(myPoints)
        imgl=createBox(img,myPoints[0:19])
        resized_img = cv2.resize(imgl, (300, 200))
    return resized_img
