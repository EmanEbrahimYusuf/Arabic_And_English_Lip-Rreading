import base64
import streamlit as st
import os 
import imageio 
import random
import tensorflow as tf

st.set_page_config(layout='wide')

st.title('Lip-Reading') 


import streamlit as st
import subprocess

def run_arabic_app():
    
    subprocess.Popen(['streamlit', 'run', 'app_arabic/Arabic.py'])

def run_english_app():
    subprocess.Popen(['streamlit', 'run', 'app_English/English.py'])


if st.button('Arabic', key='arabic-button'):
    run_arabic_app()

if st.button('English', key='english-button'):
    run_english_app()


st.markdown(
    """<style>
        .element-container:nth-of-type(2) button {
            height: 50px;
            width: 130px;
            background-color: #262730;
            color: #ffffff;
            position: fixed;
            left: calc(50% - 300px);
            top: calc(50% - 100px);
            transform: translateX(-50%);
            font-weight: bold;
            font-size: 27px;
            padding: 10px 20px;
            border-radius: 20px;
            border: 2px solid white;
            margin-right: 10px;
        }
        .element-container:nth-of-type(3) button {
            height: 50px;
            width: 130px !important;
            background-color: #262730;
            color: #ffffff;
            position: fixed;
            left: calc(50% - 300px);
            top: calc(50% - 0px);
            transform: translateX(-50%);
            font-weight: bold;
            font-size: 25px;
            padding: 10px 20px;
            border-radius: 20px;
            border: 2px solid white;
            margin-right: 10px;  
        }
    </style>""",
    unsafe_allow_html=True,
)
with st.sidebar: 
    st.image('r.png')