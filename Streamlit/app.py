import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv2 
from PIL import Image

def rotation(img, degree):
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),degree,1)
    dst = cv2.warpAffine(img_array,M,(cols,rows))
    st.image(dst)

def translation(img):
    #translation function
    #to be completed
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape

def blurring(img):
    #blurring function
    #to be completed
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape

def brightness(img):
    #function to increase/decrease the brightness of the image
    #to be completed
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape


def zoom(img):
    #function to zoom in/out the image with limit.
    #to be completed
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape


st.title('Inter IIT Tech Meet 2021')

uploaded_files = st.file_uploader("Upload images", accept_multiple_files = True)
percent_testing = st.slider('Select % of images for training', 0, 100, step=25)

rotating_degree = st.slider('Select rotation degree', -45, 45, step=1, value=0)
rotater = st.button('Rotate')
if(rotater):
    for uploaded_file in uploaded_files:
        rotation(uploaded_file, rotating_degree)
    