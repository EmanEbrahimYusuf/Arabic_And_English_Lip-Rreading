import cv2
import dlib
import numpy as np
from PIL import Image,ImageFilter
import cv2
import numpy as np
import random


def createBox(img,points):
    bbox=cv2.boundingRect(points)
    x,y,w,h=bbox
    imgcrop=img[y:y+h,x:x+w]
    imgcrop=cv2.resize(imgcrop,(0,0),None,3,3)
    return imgcrop

def detect(img,i):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("app_arabic/shape_predictor_68_face_landmarks.dat")
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector(img_gray)

    for face in faces:
        landmarks=predictor(img_gray,face)
        myPoints=[]
        for n in range(68):
            x=landmarks.part(n).x
            y=landmarks.part(n).y
            if(x>landmarks.part(61).x):
                myPoints.append([x+15,y+7])
            else:
                myPoints.append([x-15,y-7])
        # myPoints=np.array(myPoints)
        # imgl=createBox(img,myPoints[48:67])
        # resized_img = cv2.resize(imgl, (300, 200))
    return myPoints



def video2frames_func(video_path):
  capture = cv2.VideoCapture(video_path)
  cap = cv2.VideoCapture(video_path)
  frame_index = 20  
  cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
  ret, frame = cap.read()
  M_points=detect(frame,0)
  myPoints=np.array(M_points)

  capture = cv2.VideoCapture(video_path)
  frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
  fps = int(capture.get(cv2.CAP_PROP_FPS))

  if (frames>=20):
    count = 0
    images=[]
    while (True):
      
      success, frame = capture.read()
  
      if success:
        try:
          imgl=createBox(frame,myPoints[48:67])
          resized_img = cv2.resize(imgl,(300, 200))
          images.append(resized_img)
        
        except:
          continue
      elif cv2.waitKey(0):
        break
      else:
        break

      count = count+1
    capture.release()
    if (frames<60):
      for i in range(frames):
        images.insert(i*2,images[2*i])
        
        if len(images)>=60:
          break

    if (frames>60):
      while True:
        if len(images)==60:
          break
        images.pop(random.randint(0,len(images)))


    kk=cv2.imread(r'app_arabic/0.png')
    c=len(images)
    if c<60:
      for i in range(60-c):
        resized_img = cv2.resize(kk, (300, 200))
        images.append(resized_img)
        count=count+1
    cv2.destroyAllWindows()
    return images
  else:
    return
  
def preprocessing(path):
  img_array=video2frames_func(path)
  out = cv2.VideoWriter(r'pathto.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (300,200))
  for i in range(len(img_array)):
    out.write(img_array[i])
  out.release()
  return 'pathto.avi'
   