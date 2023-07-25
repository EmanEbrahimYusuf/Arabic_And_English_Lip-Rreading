
import cv2
import os 
from try2 import detect
import numpy as np
import random

def video2frames_func(video_path):
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
          images.append(detect(frame,count))
        except:
          continue
      elif cv2.waitKey(0):
        break
      else:
        break

      count = count+1
    capture.release()
    print(len(images))
    if (frames<60):
      for i in range(frames):
        print(len(images))
        images.insert(i*2,images[2*i])
        
        if len(images)>=60:
          break

    if (frames>60):
      while True:
        if len(images)==60:
          break
        images.pop(random.randint(0,len(images)))


    kk=cv2.imread(r'0.png')
    c=len(images)
    if c<60:
      for i in range(60-c):
        resized_img = cv2.resize(kk, (300, 200))
        images.append(resized_img)
        count=count+1
    cv2.destroyAllWindows()
    print('number of frames ',frames)
    print('number of process videro', len(images))
    return images
  else:
    print(f'number of freames {frames}')
    return