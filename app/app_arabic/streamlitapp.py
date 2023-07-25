
import streamlit as st
import os 
import imageio 
import random
import tensorflow as tf 
from utils import load_data, num_to_char
from modelutil import load_model


st.set_page_config(layout='wide')


with st.sidebar: 
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.info('''Arabic \n Lip-Reading''')


st.title('Arabic Lip-Reading') 

import os
import re

file_pattern = re.compile(r'.*\.avi')

root_dir = r'C:\Users\Eman\Desktop\GP_LipReading\data\Arabic_Train_Test\test'
random.seed(10)
matched_files = []
name=[]
for dirpath, dirnames, filenames in os.walk(root_dir):

    for filename in filenames:
        if file_pattern.match(filename):
            name.append(filename)
            matched_files.append(os.path.join(dirpath, filename))
random.shuffle(matched_files)

selected_video = st.selectbox('Choose video', matched_files)

col1, col2 = st.columns(2)
if matched_files: 
    

    with col1: 
        st.info('The video below displays the converted video in mp4 format')
        file_path =  selected_video
        os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')


        video = open('test_video.mp4', 'rb') 
        video_bytes = video.read() 
        st.video(video_bytes)
        video,align = load_data(tf.convert_to_tensor(file_path))
        st.info('This is the real tokens')
        st.text(align)
        st.info('Real Text')
        real = tf.strings.reduce_join(num_to_char(align)).numpy().decode('utf-8')
        st.text(real)



    with col2: 
        st.info('This is all the machine learning model sees when making a prediction')
        
        imageio.mimsave('animation.gif', video, fps=10)
        st.image('animation.gif', width=350) 
        st.info('This is the output of the machine learning model as tokens')
        model = load_model()
        yhat = model.predict(tf.expand_dims(video, axis=0))
        decoder = tf.keras.backend.ctc_decode(yhat, [60], greedy=True)[0][0].numpy()
        st.text(decoder)

        st.info('Decode the raw tokens into words')
        converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
        st.text(converted_prediction)


