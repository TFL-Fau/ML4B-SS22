import streamlit as st
import glob
from PIL import Image
import jsonlines
import pandas as pd
from pprint import pprint
import random

#Group Introduction Code
twitter=Image.open('logoOfficial.png')
philip=Image.open('Philip_Maron.jpg')
tobi=Image.open('Tobias_Fleming.jpg')
thies=Image.open('Thies_Freudenthal_Maske_neu.png')


st.set_page_config(page_icon="🐤", page_title="Twitter Sentiment Analyzer")

st.write('<base target="_blank">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    
    st.image(twitter, width=100)

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: white;'>Twitter Sentiment Analyzer </h1>",unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: white;'>Introducing group 9 with the topic Twitter Sentiment Analysis! <br> <br></h4>",unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: white;'>Our Team</h4>",unsafe_allow_html=True)

with st.expander("Click here for Team presentation", expanded=False):
    row1_1, row1_2, row1_3 = st.columns((1, 1, 1))
    with row1_1:
        st.subheader("1. Teammember")
        st.image(philip, width=215)
        st.markdown("<p style='text-align: center; color: white;'>Philip Maron <br> <br>  Eighth semester Business Informatics </p>",unsafe_allow_html=True)
    with row1_2:
        st.subheader("2. Teammember")
        st.image(tobi, width=200)
        st.markdown("<p style='text-align: center; color: white;'>Tobias Fleming <br> <br> Sixth semester Business Informatics </p>",unsafe_allow_html=True)
    with row1_3:
        st.subheader("3. Teammember")
        st.image(thies, width=219)
        st.markdown("<p front-size= 30px style='text-align: center; color: white;'>Thies Freudenthal<br> <br>Sixth semester Business Informatics </p>",unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: white;'>Projectdiscription</h4>",unsafe_allow_html=True)

with st.expander("Click here for Projectdiscription", expanded=False):
    
    st.markdown("<h5 style='text-align: center; color: white;'>Hello we are Philip, Tobias and Thies and we want to create a Twitter Sentiment Analyzer for comments of Members of the German Parliament. For this we want to use Machine Learning to process the dataset provided to us and present the results.</h5>",unsafe_allow_html=True)
    
#First Analysis of data from Olaf Scholz to get into the data

result=st.button("Generate random Olaf Scholz comment", disabled=False)
#st.write(result)

file="/Task_01/OlafScholz.jl"

texts = []
dates = []

if result:

    with jsonlines.open(file) as j: 
        for line in j:
            data=line['response']['data']
            for i in range(0, 60):
                date= data[i]['created_at']
                text= data[i]['text'] 
                dates.append(date[:10])
                texts.append(text)
                break

    randomnumber = random.randint(1, 60)

    st.write(dates[randomnumber])
    st.write(texts[randomnumber])  