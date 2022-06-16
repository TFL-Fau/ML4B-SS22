# Contents of ~/my_app/pages/page 2.py

import streamlit as st

st.set_page_config(page_icon="🕊️", page_title="German Twitter Analysis")

st.write('<base target="_blank">', unsafe_allow_html=True)

# Columns to position twitter logo in middle

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    
    st.image("twitter.png", width=100)

with col3:
    st.write(' ')

# Heading and Topic

st.write("<h1 style='text-align: center; color: white;'>Analysis of Tweets</h1>",unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: white;'>Please select a politican from one of the given political parties to show the analytic data.</h4>",unsafe_allow_html=True)

# Selecting political party and politician

optionpp = st.selectbox(
     'Political Party',
     ('- Select -', 'AFD', 'CDU/CSU', 'SPD', 'Bündnis90/Die Grünen', 'Die Linke', 'FDP'))

if optionpp=='AFD':
   st.write('You selected the political party:', optionpp + ".")
   optionafd = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('- Select -', 'Tino Chrupalla', 'Dr. Alice Weidel', 'Beatrix von Storch'))
elif optionpp=='CDU/CSU':
   st.write('You selected the political party:', optionpp + ".")
   optioncducsu = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('- Select -', 'Daniela Ludwig', 'Andreas Scheuer', 'Friedrich Merz', 'Philip Amthor', 'Jens Spahn', 'Julia Klöckner', 'Armin Laschet'))
elif optionpp=='SPD':
   st.write('You selected the political party:', optionpp + ".")
   optionspd = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('- Select -', 'Olaf Scholz', 'Christine Lambrecht', 'Saskia Esken', 'Kevin Kühnert', 'Prof. Dr. Karl Lauterbach'))
   # Data of SPD politicians

   # First Olaf Scholz

   if optionspd == 'Olaf Scholz':  
        st.write('You selected the politician:', optionspd + ".")
        st.write('Time needed to process data: 04:30,89 min.')
        st.write(" ")
        st.write(" ")
        st.write("<h3 style='text-align: center; color: white;'>Olaf Scholz Twitter Data Analysis</h3>",unsafe_allow_html=True)
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>1. Overview about the number of tweets over time</h4>",unsafe_allow_html=True)
        st.image("spd/scholz/os1.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>2. Get a first overview over the used words in the tweets.</h4>",unsafe_allow_html=True)
        st.image("spd/scholz/os2.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>3. Cleaning the text of the dataframe for further processing.</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Changed ÄÜÖäüö to AeUeOEaeueoe")
        st.write("- Saved cleaned data in new column named edited")
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>4. Cleaning the text for sentiment analysis</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Saved cleaned data in new column named textforttb")
        
        st.write("<h4 style='text-align: center; color: white;'>5. Show Wordcloud with cleaned text</h4>",unsafe_allow_html=True)
        st.image("spd/scholz/os3.png", width=800)
       
        st.write("<h4 style='text-align: center; color: white;'>6. Sentiment Analysis with TextBlob</h4>",unsafe_allow_html=True)
        st.write("- Get the Subjectivity for each tweet: Subjectivity quantifies the amount of personal opinion and factual information contained in the text. The higher subjectivity means that the text contains personal opinion rather than factual information. 0 means low personal opinion and 1 a lot of personal opinion.") 
        st.write("- Save Subjectivity in new column named Personal Opinion (Subjectivity)")
        st.write("- Get the Polarity for each tweet: Polarity lies between [-1,1], -1 defines a negative sentiment and 1 defines a positive sentiment")
        st.write("- Save Polarity in new column named Sentiment (Polarity)")
        st.write("Create new column named Analysis where an Intepration of the the Polarity is saved.")
        st.write("- A score below -0.15 is considered as a negative tweet")
        st.write("- A score between -0.15 and 0.15 is considered as a neutral tweet")
        st.write("- A score above 0.15 is considered as a positive tweet")
        st.write("Show a Scatterplot for both results:")
        st.image("spd/scholz/os4.png", width=800)
        st.write("Show the percentage of each polarity as numbers and diagram:")
        st.image("spd/scholz/os5.png", width=800)
        st.image("spd/scholz/os6.png", width=800)
        st.write("Show the polarity and subjectivty of tweets over time:")
        st.image("spd/scholz/os7.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>8. Word related analysis</h4>",unsafe_allow_html=True)
        st.write("Show the amount of words per tweet:")
        st.image("spd/scholz/os8.png", width=800)
        st.write("Show a list of the most frequent words:")
        st.image("spd/scholz/os9.png", width=800)
        st.write("Show a list of the most frequent trigram ofwords:")
        st.image("spd/scholz/os10.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>9. Topic Analysis with LDA and Bertopic</h4>",unsafe_allow_html=True)
        st.write("Result of the LDA analysis:")
        st.image("spd/scholz/os11.png", width=800)
        st.write("Result of the Topic Modelling with Bertopic:")
        st.image("spd/scholz/os12.png", width=800)
        st.image("spd/scholz/os13.png", width=800)
        st.image("spd/scholz/os14.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>10. Emotion Analysis</h4>",unsafe_allow_html=True)
        st.write("Steps to take to connect tweets with emotions")
        st.write("1. Create a list of words were the emotion of each is entered as a 0 or 1")
        st.write("2. Go threw every tweets and count the the times a word of each emotion appears")
        st.write("3. Save in a new column for each emotion the number of times the emotion appears in the tweet")
        st.write("Show the top 15 words for every emotion: ")
        st.image("spd/scholz/os15.png", width=800)
        st.image("spd/scholz/os16.png", width=800)
        st.image("spd/scholz/os17.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>11. Connect Sentiment and Emotion Analysis for Comparison</h4>",unsafe_allow_html=True)
        st.write("Declare Freude, Vorfreude, Vertrauen and Überraschung as positive emotions.")
        st.write("Declare Traurigkeit, Furcht, Ekel and Wut as negative emotions.")
        st.write("Count the total number of times a negative or positive emotion accurs in a tweet and save the number in two extra columns.")
        st.write("Go threw each tweet and safe in a new column if there are more then 0 total negative or positive emotions.")
        st.write(" ")
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a negative emotion:")
        st.image("spd/scholz/os18.png", width=800)
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a positive emotion:")
        st.image("spd/scholz/os19.png", width=800)
        st.write("Show the percentage of tweets which share the emotion and sentiment:")
        st.image("spd/scholz/os20.png", width=800)
        st.image("spd/scholz/os21.png", width=800)
        
elif optionpp=='Bündnis90/Die Grünen':
   st.write('You selected the political party:', optionpp + ".")
   optiongruenen = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('- Select -', 'Renate Künast', 'Annalena Baerbock', 'Katrin Göring-Eckardt', 'Cem Özdemir'))
elif optionpp=='Die Linke':
   st.write('You selected the political party:', optionpp + ".")
   optionlinke = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('- Select -', 'Dr. Dietmar Bartsch', 'Dr. Gregor Gysi', 'Susanne Henning-Wellsow', 'Janine Wissler'))
elif optionpp=='FDP':
   st.write('You selected the political party:', optionpp + ".")
   optionfdp = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('- Select -', 'Christian Lindner', 'Dr. Marco Buschmann', 'Volker Wissing'))

    
    

