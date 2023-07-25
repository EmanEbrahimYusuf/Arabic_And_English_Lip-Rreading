import cv2
import dlib
import numpy as np
from PIL import Image, ImageFilter
import concurrent.futures
import random
import time
from skimage.transform import resize

import numpy as np
import random

np.random.seed(123)
random.seed(123)

def createBox(img, points):
    bbox = cv2.boundingRect(points)
    x, y, w, h = bbox
    imgcrop = img[y:y+h, x:x+w]
    imgcrop = cv2.resize(imgcrop, (0, 0), None, 3, 3)
    return imgcrop


def detect(img, i):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("app_arabic/shape_predictor_68_face_landmarks.dat")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(img_gray)

    for face in faces:
        landmarks = predictor(img_gray, face)
        myPoints = []
        for n in range(48, 59):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            if(x > landmarks.part(61).x):
                myPoints.append([x+15, y+7])
            else:
                myPoints.append([x-15, y-7])
        myPoints = np.array(myPoints)
        imgl = createBox(img, myPoints[0:11])
        resized_img = cv2.resize(imgl, (300, 200))
    return resized_img

def detect_parallel(args):
    img, i = args
    return detect(img, i)

import multiprocessing

def video2frames_func_parallel(video_path):
    capture = cv2.VideoCapture(video_path)
    frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(capture.get(cv2.CAP_PROP_FPS))

    if frames >= 20:
        images = []
        pool = multiprocessing.Pool(processes=5)
        results = []
        for i in range(frames):
            success, frame = capture.read()
            if success:
                results.append(pool.apply_async(detect, args=(frame, i)))
            else:
                break
        pool.close()
        pool.join()
        for result in results:
            try:
                img = result.get()
                images.append(img)
            except Exception as e:
                print('Error while processing frame:', e)

        capture.release()
        if frames < 60:
            for i in range(frames):
                if 2*i < len(images):
                    images.insert(i*2, images[2*i])
                if len(images) >= 60:
                    break
        elif frames > 60:
            for i in reversed(range(len(images))):
                if len(images) == 60:
                    break
                if i%2 == 0:
                    images.pop(i)

        kk = cv2.imread(r'app_arabic/0.png')
        c = len(images)
        if c < 60:
            for i in range(60-c):
                resized_img = resize(kk, (200, 300), anti_aliasing=True)
                images.append(resized_img)

        return images
    else:
        return
        return

def preprocessing(path):
    start_time = time.time()
    img_array = video2frames_func_parallel(path)
    out = cv2.VideoWriter(r'path.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (300, 200))
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    end_time = time.time()
    print("***********************************************************")
    print("Preprocessing time:____________________________________", end_time - start_time, "seconds")
    print("***********************************************************")
    return 'path.avi',(end_time - start_time)

