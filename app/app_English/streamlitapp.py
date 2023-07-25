
import streamlit as st
import os 
import imageio 

import tensorflow as tf 
from utils import load_data, num_to_char
from modelutil import load_model


st.set_page_config(layout='wide')

with st.sidebar: 
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.info('''English  \n Lip-Reading''')
    

st.title('English Lip-Reading') 

options = os.listdir(os.path.join(r'C:\Users\Eman\Desktop\GP_LipReading\data\Test_Eng\1','videos'))
selected_video = st.selectbox('Choose video', options)


col1, col2 = st.columns(2)

if options: 


    with col1: 
        st.info('The video below displays the converted video in mp4 format')
        file_path = os.path.join(r'C:\Users\Eman\Desktop\GP_LipReading\data\Test_Eng\1','videos', selected_video)
        os.system(f'ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')

        
        video = open('test_video.mp4', 'rb') 
        video_bytes = video.read() 
        st.video(video_bytes)
        video, align = load_data(tf.convert_to_tensor(file_path))

    with col2: 
        st.info('This is all the machine learning model sees when making a prediction')

        imageio.mimsave('animation.gif', video, fps=10)
        st.image('animation.gif', width=400) 

        st.info('This is the output of the machine learning model as tokens')
        model = load_model()
        yhat = model.predict(tf.expand_dims(video, axis=0))
        decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
        st.text(decoder)

      
        st.info('Decode the raw tokens into words')
        converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
        st.text(converted_prediction)
        
