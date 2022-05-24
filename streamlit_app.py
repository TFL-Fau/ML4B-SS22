import streamlit as st
import jsonlines
import random
import pandas as pd
from PIL import Image

#Group Introduction Code

st.set_page_config(page_icon="🐤", page_title="Sentiment Analysis of Tweets")

st.write('<base target="_blank">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    
    st.image("twitter.png", width=100)

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: white;'>Sentiment Analysis of Tweets</h1>",unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: white;'>Introducing group 9 with the topic Sentiment Analysis of Tweets! <br> <br></h4>",unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: white;'>Our Team</h4>",unsafe_allow_html=True)

with st.expander("Click here for Team presentation", expanded=False):
    row1_1, row1_2, row1_3 = st.columns((1, 1, 1))
    with row1_1:
        st.subheader("1. Teammember")
        st.image("Philip.jpg", width=215)
        st.markdown("<p style='text-align: center; color: white;'>Philip Maron <br> <br>  Eighth semester Business Informatics </p>",unsafe_allow_html=True)
    with row1_2:
        st.subheader("2. Teammember")
        st.image("Tobias.jpg", width=200)
        st.markdown("<p style='text-align: center; color: white;'>Tobias Fleming <br> <br> Sixth semester Business Informatics </p>",unsafe_allow_html=True)
    with row1_3:
        st.subheader("3. Teammember")
        st.image("Thies.png", width=219)
        st.markdown("<p front-size= 30px style='text-align: center; color: white;'>Thies Freudenthal<br> <br>Sixth semester Business Informatics </p>",unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: white;'>Projectdiscription</h4>",unsafe_allow_html=True)

with st.expander("Click here for Projectdiscription", expanded=False):
    
    st.markdown("<h5 style='text-align: center; color: white;'>Hello we are Philip, Tobias and Thies and we want to create a Twitter Sentiment Analyzer for comments of Members of the German Parliament. For this we want to use Machine Learning to process the dataset provided to us and present the results.</h5>",unsafe_allow_html=True)
    
#First Analysis of data from Olaf Scholz to get into the data and generating random Olar Scholz comment

st.write(' ')
result=st.button("Generate random Olaf Scholz comment", disabled=False)
#st.write(result)

file="OlafScholz.jl"

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
with st.expander("Analyzing given Dataset", expanded=False):
    # Analyzing given dataset

    st.markdown("<h4 style='text-align: center; color: white;'>Analysing Dataset for our Dataframe</h4>",unsafe_allow_html=True)
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
    st.write('Parameters filtered for new dataframe: ')
    st.write('- target: To store the outcome of our analysis')
    st.write('- tweetid: Given from response, data and id')
    st.write('- user: Given from response, data and author_id')
    st.write('- date: Given from response, data and created at')
    st.write('- time: Given from response, data and created at')
    st.write('- text: Given from response, data and text')
    
with st.expander("Show our dataframe", expanded=False):
    # Creating dataframe

    st.markdown("<h4 style='text-align: center; color: white;'>Our Dataframe</h4>",unsafe_allow_html=True)
    st.write(' ')
    
        olafScholzJsonLines = jsonlines.open("OlafScholz.jl")
        df = pd.DataFrame(columns = ["target", "tweetid", "date", "time", "user", "text"])
  
        iterator = 0

        for line in olafScholzJsonLines:
            keyResponse = line["response"]
            data = keyResponse["data"]
            newDataRow = [None, None, None, None, None, None]
            userName = line["account_name"]
            newDataRow[4] = userName
            keyResponse = line["response"]
            data = keyResponse["data"]


            for tweet in data:
             
                tweetTarget = None
                tweetID = tweet["id"]
                authorID = tweet["author_id"]
                tweetDate = tweet["created_at"][0:10]
                tweetTime = tweet["created_at"][11:19]
                tweetText = tweet["text"]
                newDataRow[0] = tweetTarget
                newDataRow[1] = tweetID
                newDataRow[2] = tweetDate
                newDataRow[3] = tweetTime
                #
                newDataRow[4] = authorID
                newDataRow[5] = tweetText
                
                df.loc[len(df)] = newDataRow
                
            iterator += 1
        st.write('Anzahl an Zeilen und Spalten')
        st.write(df.shape)
        st.write(df.head(20))

with st.expander("Analyze data from Dataframe", expanded=False):
    # Creating dataframe

    st.markdown("<h4 style='text-align: center; color: white;'>Analyze data from Dataframe</h4>",unsafe_allow_html=True)
    st.write(' ')
    showa=st.button("Show analyze", disabled=False)
    if showa:
          
        olafScholzJsonLines = jsonlines.open("OlafScholz.jl")
        df = pd.DataFrame(columns = ["target", "tweetid", "date", "time", "user", "text"])
  
        iterator = 0

        for line in olafScholzJsonLines:
            keyResponse = line["response"]
            data = keyResponse["data"]
            newDataRow = [None, None, None, None, None, None]
            userName = line["account_name"]
            newDataRow[4] = userName
            keyResponse = line["response"]
            data = keyResponse["data"]


            for tweet in data:
             
                tweetTarget = None
                tweetID = tweet["id"]
                authorID = tweet["author_id"]
                tweetDate = tweet["created_at"][0:10]
                tweetTime = tweet["created_at"][11:19]
                tweetText = tweet["text"]
                newDataRow[0] = tweetTarget
                newDataRow[1] = tweetID
                newDataRow[2] = tweetDate
                newDataRow[3] = tweetTime
                #
                newDataRow[4] = authorID
                newDataRow[5] = tweetText
                
                df.loc[len(df)] = newDataRow
                
            iterator += 1
        st.write('First date:')
        st.write(df['date'].min())
        st.write('Last date:')
        st.write(df['date'].max())

        image = Image.open('dataframepic.png')

        st.image(image, caption='Number of tweets per year')
    
    
    
    
    
            