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

def translation(img, tx, ty):
    #translation function
    #to be completed
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape
    
    ## code 
    
    M = np.float32([1,0,tx] , [0,1,ty])
    shifted = cv2.warpAffine(img_array,M,(cols,rows))
    st.image(shifted)
    
    
    ##code

def blurring(img):
    #blurring function
    #to be completed
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape
    
    ##code - Gausian Blurring
    gausBlur = cv2.GaussianBlur(img_array, (5,5),0)
    
    
    ##code

def brightness(img):
    #function to increase/decrease the brightness of the image
    #to be completed
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape
    
    ##code 
    
    ##code

def zoom(img, width, height):
    #function to zoom in/out the image with limit.
    #to be completed
    image = Image.open(img)
    img_array = np.array(image)    
    rows,cols, temp = img_array.shape
    
    ##code interpolation 

    stretch_near = cv2.resize(image_array, (width, height),interpolation = cv2.INTER_NEAREST)
    ##code
    


st.title('Inter IIT Tech Meet 2021')

uploaded_files = st.file_uploader("Upload images", accept_multiple_files = True)
percent_testing = st.slider('Select % of images for training', 0, 100, step=25)

rotating_degree = st.slider('Select rotation degree', -45, 45, step=1, value=0)
rotater = st.button('Rotate')
if(rotater):
    for uploaded_file in uploaded_files:
        rotation(uploaded_file, rotating_degree)
    
