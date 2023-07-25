import cv2
import numpy as np
import glob
import os
import random

classes=os.listdir('numbers')
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
          framess=cv2.resize(frame, (300, 200))
          images.append(framess)
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
      

    # kk=cv2.imread('0.png')
    # c=count
    # if c<60:
    #   for i in range(60-c):
    #     resized_img = cv2.resize(kk, (300, 200))
    #     images.append(resized_img)
    #     count=count+1
    cv2.destroyAllWindows()
    return images
  else:
    print(f'number of freames {frames}')
    return


for cls in classes:
    list_vid=os.listdir(os.path.join('numbers', cls))
    try:
        os.mkdir(f'numbers60/{cls}')
    except:
        continue
    for i , name in enumerate(list_vid):

        try:
            print(name)
            print(f'numbers/{cls}\\'+name)
            img_array=video2frames_func(f'numbers/{cls}\\'+name)
            print(len(img_array))
            out = cv2.VideoWriter(f'numbers60/{cls}/'+name,cv2.VideoWriter_fourcc(*'DIVX'), 30, (300,200))
            for i in range(len(img_array)):
                out.write(img_array[i])
            out.release()
           
        except:
            continue

