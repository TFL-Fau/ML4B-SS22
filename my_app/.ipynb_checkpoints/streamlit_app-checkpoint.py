# Contents of ~/my_app/main_page.py

import streamlit as st
import jsonlines
import random
import pandas as pd

from PIL import Image

#Group Introduction Code

st.set_page_config(page_icon="🕊️", page_title="German Twitter Analysis")

st.write('<base target="_blank">', unsafe_allow_html=True)

# Columns to position twitter logo in middle

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    
    st.image("my_app/twitter.png", width=100)

with col3:
    st.write(' ')

# Heading and Topic

st.write("<h1 style='text-align: center;'>Sentiment Analysis of Tweets</h1>",unsafe_allow_html=True)

st.write("<h4 style='text-align: center;'>Introducing group 9 with the topic Sentiment Analysis of Tweets! <br> <br></h4>",unsafe_allow_html=True)

# Project Description

st.write("<h3 style='text-align: center;'>Projectdescription & Team </h3>",unsafe_allow_html=True)
st.write("<h5 style='text-align: center;'>Hello, we are Philip, Tobias, and Thies. We created a Twitter Sentiment Analyzer for tweets and comments of members of the German Parliament. For this, we used Machine Learning to analyze and process tweets and present the results.</h5>",unsafe_allow_html=True)
row1_1, row1_2, row1_3 = st.columns((1, 1, 1))
with row1_1:
    st.image("my_app/Philip.jpg", width=215)
    st.write("<p style='text-align: center;'>Philip Maron <br> <br>  Eighth semester Business Informatics </p>",unsafe_allow_html=True)
with row1_2:
    st.image("my_app/Tobias.jpg", width=200)
    st.write("<p style='text-align: center;'>Tobias Fleming <br> <br> Sixth semester Business Informatics </p>",unsafe_allow_html=True)
with row1_3:
    st.image("my_app/Thies.png", width=219)
    st.write("<p front-size= 30px style='text-align: center;'>Thies Freudenthal<br> <br>Sixth semester Business Informatics </p>",unsafe_allow_html=True)
    
#First Analysis of data from Olaf Scholz to get into the data and generating random Olar Scholz comment

with st.expander("1. Task: Get random Olaf Scholz comment from dataset", expanded=False):
    st.write(' ')
    result=st.button("Get your Olaf Scholz comment from dataset", disabled=False)
    #st.write(result)

    file="my_app/OlafScholz.jl"

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

# Analyzing given Data and creating Dataframe
        
with st.expander("2. Task: Analyzing given Data and creating Dataframe", expanded=False):
    # Analyzing given dataset

    st.write("<h4 style='text-align: center;'>Analysing Dataset for our Dataframe</h4>",unsafe_allow_html=True)
    st.write(' ')
    st.write('- Analyzing the given Dataset')
    st.write('- Looking for useful parameters to create a dataset')
    st.write(' ')
    showana=st.button("Show Dataset Analysis", disabled=False)
    
    if showana:
        with jsonlines.open(file) as j:
            for line in j:
                 st.write('Typ: ')
                 st.write(type(line))
                 st.write('Keys des Datensatzes: ')
                 st.write(line.keys())
                 st.write('Keys von response: ')
                 st.write(line['response'].keys())
                 st.write('Keys von data in response: ')
                 st.write(line['response']['data'][0].keys())
                 break
    st.write('Parameters filtered for dataframe: ')
    st.write('- tweetid: Given from response, data and id')
    st.write('- datetime: Given from response, data and created at')
    st.write('- date: Given from response, data and created at')
    st.write('- time: Given from response, data and created at')
    st.write('- user: Given from response, data and author_id')
    st.write('- text: Given from response, data and text')
    

#image = Image.open('dataframepic.png')
#st.image(image, caption='Number of tweets per year')

# Preprocessing of our Dataframe

with st.expander("3. Task: Preprocessing of our Dataframe", expanded=False):

    st.write("<h4 style='text-align: center;'>Preprocessing of our Dataframe</h4>",unsafe_allow_html=True)
    st.write('- Converted the datetime column with pd.to_datetime to use for diagrams etc.')
    st.write('- Removed Retweets from the dataframe')
    st.write('- Checked the language of the tweets')
    st.write('- Added the language of the tweet in a new column')
    st.write('- Removed the non german tweets')

# Goals for the Data Analysis of tweets  

with st.expander("4. Task: Goals for the Data Analysis of tweets", expanded=False):

    st.write("<h4 style='text-align: center;'>Goals for the Data Analysis of tweets</h4>",unsafe_allow_html=True)
    st.write('Our Goal: ')
    st.write('- Visualize used words and content in different ways')
    st.write('- Sentiment and Polarity Analysis')
    st.write('- Latent Dirichlet Allocation (LDA)')
    st.write('- Topic Modeling')
    st.write('- Emotion Analysis')
    st.write('- Comparison and Contrast of sentiment and emotion analysis')
    st.write('- Creating an algorithm for detecting emotions in a tweet')
    st.write('- Compare different machine learning algorithms in performance')
    st.write(' ')
    st.write('On the page "Analysis of Tweets" we analyzed the tweets of many politicians from every political party in the german bundestag 2022.')
    st.write('All data was processed with an Apple Macbook Pro with an Apple M1 chip with 16gb RAM.')
          
