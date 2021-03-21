import streamlit as sl
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import cv2 as cv2 
from PIL import Image

#data=pd.read_csv("#name of CSV",width=,height=)'
A=[1,2,3,4,5,6,7,8,9,10]
N=np.array(A)

A_d=N.reshape(2,5)

sl.dataframe(A_d)

data=pd.DataFrame(np.random.randn(100,3))
#sl.table(dic)
#sl.json(dic)
sl.line_chart(data)
sl.area_chart(data)
sl.bar_chart(data)


#uploaded_file = sl.file_uploader("Choose a file")


#if uploaded_file is not None:
#    sl.image(uploaded_file)
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     sl.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     sl.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     sl.write(string_data)

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     sl.write(dataframe)


uploaded_files = sl.file_uploader("Choose images file", accept_multiple_files=True)

if len(uploaded_files)!=0:
    test_images = sl.slider('Kitne aadmi the', 0, len(uploaded_files)-1, 1)


#sl.image(uploaded_files[0])

# for uploaded_file in uploaded_files:
#     sl.image(uploaded_file)
    
    # bytes_data = uploaded_file.read()
    # sl.write("filename:", uploaded_file.name)
    # sl.write(bytes_data)

#flip: 
sl.write(uploaded_files)
for uploaded_file in uploaded_files:
    
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    #sl.write(img_array)
    # img_array = img_array.astype(np.uint8)
    # img_red, img_green, img_blue = img_array
    # rgb = np.dstack([img_red, img_green, img_blue])
    
    rows,cols, temp = img_array.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
    dst = cv2.warpAffine(img_array,M,(cols,rows))
    sl.image(dst)
    






# for uploaded_file in uploaded_files:
#     im = cv2.imread(uploaded_file.name)
#     flip=cv2.flip(im,1)
#     plt.imshow(flip)
#     #rotation:
#     img = cv2.imread(uploaded_file.name)
#     rows,cols, temp = img.shape

#     M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
#     dst = cv2.warpAffine(img,M,(cols,rows))
#     sl.image(dst)

#     #Translation:

#     img=cv2.imread(uploaded_file.name)
#     rows,cols,temp = img.shape

#     M = np.float32([[1,0,0],[0,1,0]])
#     dst = cv2.warpAffine(img,M,(cols,rows))
#     plt.imshow(dst)
