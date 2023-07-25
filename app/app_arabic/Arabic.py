import streamlit as st
import pandas as pd
import base64
import streamlit as st
import os
import imageio
import random
import tensorflow as tf
from utils import load_data2, num_to_char
from modelutil import load_model
from pip_line2 import preprocessing
import pandas as pd


with st.sidebar: 
    st.image('r.png')
    st.info('''Arabic \n Lip-Reading''')
   

st.title('Arabic Lip-Reading') 


import os
import re

file_pattern = re.compile(r'.*\.avi')

def save_uploaded_file(uploaded_file): 
    
    with open("temp.mp4", "wb") as f: 
        f.write(uploaded_file.getbuffer()) 
        return "temp.mp4"


video_file = st.file_uploader("Upload a video file", type=[])

if video_file: 
    file_path = video_file.name
    vid = save_uploaded_file(video_file)
    vidto, time = preprocessing(vid)
    time = round(time, 2)
    os.system(f'ffmpeg -i {vidto} -vcodec libx264 test_video.mp4 -y')
    os.system(f'ffmpeg -i {vid} -vcodec libx264 test_vo.mp4 -y')
    video = open('test_vo.mp4', 'rb') 
    video_bytes = video.read() 
    st.video(video_bytes)
    video = load_data2(tf.convert_to_tensor('test_video.mp4'))
    model = load_model()
    yhat = model.predict(tf.expand_dims(video, axis=0))
    decoder = tf.keras.backend.ctc_decode(yhat, [60], greedy=True)[0][0].numpy()
    converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
    st.write(f"<span style='color:#1B6B93; font-weight: bold;'>Video text :   </span> <span style='color:white; font-weight: bold;'>{converted_prediction}</span>", unsafe_allow_html=True)
    
    
    
