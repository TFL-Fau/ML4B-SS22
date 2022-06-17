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
 
# Alice Weidel

   if optionafd == 'Dr. Alice Weidel':  
        st.write('You selected the politician:', optionafd + ".")
        st.write('Time needed to process data: 03:34,39 min.')
        st.write('Number of tweets: 2227.')
        st.write(" ")
        st.write(" ")
        st.write("<h3 style='text-align: center; color: white;'>Olaf Scholz Twitter Data Analysis</h3>",unsafe_allow_html=True)
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>1. Overview about the number of tweets over time</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/afd/weidel/wd1.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>2. Get a first overview over the used words in the tweets.</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/afd/weidel/wd2.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>3. Cleaning the text of the dataframe for further processing.</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Changed ÄÜÖäüö to AeUeOEaeueoe")
        st.write("- Saved cleaned data in new column named edited")
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>4. Cleaning the text for sentiment analysis</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Saved cleaned data in new column named textforttb")
        
        st.write("<h4 style='text-align: center; color: white;'>5. Show Wordcloud with cleaned text</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/afd/weidel/wd3.png", width=800)
       
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
        st.image("Analytics_Result/afd/weidel/wd4.png", width=800)
        st.write("Show the percentage of each polarity as numbers and diagram:")
        st.image("Analytics_Result/afd/weidel/wd5.png", width=800)
        st.image("Analytics_Result/afd/weidel/wd6.png", width=800)
        st.write("Show the polarity and subjectivty of tweets over time:")
        st.image("Analytics_Result/afd/weidel/wd7.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>8. Word related analysis</h4>",unsafe_allow_html=True)
        st.write("Show the amount of words per tweet:")
        st.image("Analytics_Result/afd/weidel/wd8.png", width=800)
        st.write("Show a list of the most frequent words:")
        st.image("Analytics_Result/afd/weidel/wd9.png", width=800)
        st.write("Show a list of the most frequent trigram ofwords:")
        st.image("Analytics_Result/afd/weidel/wd10.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>9. Topic Analysis with LDA and Bertopic</h4>",unsafe_allow_html=True)
        st.write("Result of the LDA analysis:")
        st.image("Analytics_Result/afd/weidel/wd11.png", width=800)
        st.write("Result of the Topic Modelling with Bertopic:")
        st.image("Analytics_Result/afd/weidel/wd12.png", width=800)
        st.image("Analytics_Result/afd/weidel/wd13.png", width=800)
        st.image("Analytics_Result/afd/weidel/wd14.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>10. Emotion Analysis</h4>",unsafe_allow_html=True)
        st.write("Steps to take to connect tweets with emotions")
        st.write("1. Create a list of words were the emotion of each is entered as a 0 or 1")
        st.write("2. Go threw every tweets and count the the times a word of each emotion appears")
        st.write("3. Save in a new column for each emotion the number of times the emotion appears in the tweet")
        st.write("Show the top 15 words for every emotion: ")
        st.image("Analytics_Result/afd/weidel/wd15.png", width=800)
        st.image("Analytics_Result/afd/weidel/wd16.png", width=800)
        st.image("Analytics_Result/afd/weidel/wd17.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>11. Connect Sentiment and Emotion Analysis for Comparison</h4>",unsafe_allow_html=True)
        st.write("Declare Freude, Vorfreude, Vertrauen and Überraschung as positive emotions.")
        st.write("Declare Traurigkeit, Furcht, Ekel and Wut as negative emotions.")
        st.write("Count the total number of times a negative or positive emotion accurs in a tweet and save the number in two extra columns.")
        st.write("Go threw each tweet and safe in a new column if there are more then 0 total negative or positive emotions.")
        st.write(" ")
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a negative emotion:")
        st.image("Analytics_Result/afd/weidel/wd18.png", width=800)
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a positive emotion:")
        st.image("Analytics_Result/afd/weidel/wd19.png", width=800)
        st.write("Show the percentage of tweets which share the emotion and sentiment:")
        st.image("Analytics_Result/afd/weidel/wd20.png", width=800)
        st.image("Analytics_Result/afd/weidel/wd21.png", width=800)    
    
    
elif optionpp=='CDU/CSU':
   st.write('You selected the political party:', optionpp + ".")
   optioncducsu = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('- Select -', 'Daniela Ludwig', 'Andreas Scheuer', 'Friedrich Merz', 'Philip Amthor', 'Jens Spahn', 'Julia Klöckner', 'Armin Laschet'))
elif optionpp=='SPD':
   st.write('You selected the political party:', optionpp + ".")
   optionspd = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('- Select -', 'Olaf Scholz', 'Kevin Kühnert',  'Prof. Dr. Karl Lauterbach', 'Saskia Esken'))
   # Data of SPD politicians

   # Olaf Scholz

   if optionspd == 'Olaf Scholz':  
        st.write('You selected the politician:', optionspd + ".")
        st.write('Time needed to process data: 04:30,89 min.')
        st.write('Number of tweets: 4119.')
        st.write(" ")
        st.write(" ")
        st.write("<h3 style='text-align: center; color: white;'>Olaf Scholz Twitter Data Analysis</h3>",unsafe_allow_html=True)
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>1. Overview about the number of tweets over time</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/scholz/os1.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>2. Get a first overview over the used words in the tweets.</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/scholz/os2.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>3. Cleaning the text of the dataframe for further processing.</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Changed ÄÜÖäüö to AeUeOEaeueoe")
        st.write("- Saved cleaned data in new column named edited")
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>4. Cleaning the text for sentiment analysis</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Saved cleaned data in new column named textforttb")
        
        st.write("<h4 style='text-align: center; color: white;'>5. Show Wordcloud with cleaned text</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/scholz/os3.png", width=800)
       
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
        st.image("Analytics_Result/spd/scholz/os4.png", width=800)
        st.write("Show the percentage of each polarity as numbers and diagram:")
        st.image("Analytics_Result/spd/scholz/os5.png", width=800)
        st.image("Analytics_Result/spd/scholz/os6.png", width=800)
        st.write("Show the polarity and subjectivty of tweets over time:")
        st.image("Analytics_Result/spd/scholz/os7.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>8. Word related analysis</h4>",unsafe_allow_html=True)
        st.write("Show the amount of words per tweet:")
        st.image("Analytics_Result/spd/scholz/os8.png", width=800)
        st.write("Show a list of the most frequent words:")
        st.image("Analytics_Result/spd/scholz/os9.png", width=800)
        st.write("Show a list of the most frequent trigram ofwords:")
        st.image("Analytics_Result/spd/scholz/os10.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>9. Topic Analysis with LDA and Bertopic</h4>",unsafe_allow_html=True)
        st.write("Result of the LDA analysis:")
        st.image("Analytics_Result/spd/scholz/os11.png", width=800)
        st.write("Result of the Topic Modelling with Bertopic:")
        st.image("Analytics_Result/spd/scholz/os12.png", width=800)
        st.image("Analytics_Result/spd/scholz/os13.png", width=800)
        st.image("Analytics_Result/spd/scholz/os14.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>10. Emotion Analysis</h4>",unsafe_allow_html=True)
        st.write("Steps to take to connect tweets with emotions")
        st.write("1. Create a list of words were the emotion of each is entered as a 0 or 1")
        st.write("2. Go threw every tweets and count the the times a word of each emotion appears")
        st.write("3. Save in a new column for each emotion the number of times the emotion appears in the tweet")
        st.write("Show the top 15 words for every emotion: ")
        st.image("Analytics_Result/spd/scholz/os15.png", width=800)
        st.image("Analytics_Result/spd/scholz/os16.png", width=800)
        st.image("Analytics_Result/spd/scholz/os17.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>11. Connect Sentiment and Emotion Analysis for Comparison</h4>",unsafe_allow_html=True)
        st.write("Declare Freude, Vorfreude, Vertrauen and Überraschung as positive emotions.")
        st.write("Declare Traurigkeit, Furcht, Ekel and Wut as negative emotions.")
        st.write("Count the total number of times a negative or positive emotion accurs in a tweet and save the number in two extra columns.")
        st.write("Go threw each tweet and safe in a new column if there are more then 0 total negative or positive emotions.")
        st.write(" ")
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a negative emotion:")
        st.image("Analytics_Result/spd/scholz/os18.png", width=800)
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a positive emotion:")
        st.image("Analytics_Result/spd/scholz/os19.png", width=800)
        st.write("Show the percentage of tweets which share the emotion and sentiment:")
        st.image("Analytics_Result/spd/scholz/os20.png", width=800)
        st.image("Analytics_Result/spd/scholz/os21.png", width=800)

# Kevin Kuehnert

   if optionspd == 'Kevin Kühnert':  
        st.write('You selected the politician:', optionspd + ".")
        st.write('Time needed to process data: 07:48,31 min.')
        st.write('Number of tweets: 8376.')
        st.write(" ")
        st.write(" ")
        st.write("<h3 style='text-align: center; color: white;'>Olaf Scholz Twitter Data Analysis</h3>",unsafe_allow_html=True)
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>1. Overview about the number of tweets over time</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/kuehnert/ku1.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>2. Get a first overview over the used words in the tweets.</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/kuehnert/ku2.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>3. Cleaning the text of the dataframe for further processing.</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Changed ÄÜÖäüö to AeUeOEaeueoe")
        st.write("- Saved cleaned data in new column named edited")
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>4. Cleaning the text for sentiment analysis</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Saved cleaned data in new column named textforttb")
        
        st.write("<h4 style='text-align: center; color: white;'>5. Show Wordcloud with cleaned text</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/kuehnert/ku3.png", width=800)
       
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
        st.image("Analytics_Result/spd/kuehnert/ku4.png", width=800)
        st.write("Show the percentage of each polarity as numbers and diagram:")
        st.image("Analytics_Result/spd/kuehnert/ku5.png", width=800)
        st.image("Analytics_Result/spd/kuehnert/ku6.png", width=800)
        st.write("Show the polarity and subjectivty of tweets over time:")
        st.image("Analytics_Result/spd/kuehnert/ku7.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>8. Word related analysis</h4>",unsafe_allow_html=True)
        st.write("Show the amount of words per tweet:")
        st.image("Analytics_Result/spd/kuehnert/ku8.png", width=800)
        st.write("Show a list of the most frequent words:")
        st.image("Analytics_Result/spd/kuehnert/ku9.png", width=800)
        st.write("Show a list of the most frequent trigram ofwords:")
        st.image("Analytics_Result/spd/kuehnert/ku10.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>9. Topic Analysis with LDA and Bertopic</h4>",unsafe_allow_html=True)
        st.write("Result of the LDA analysis:")
        st.image("Analytics_Result/spd/kuehnert/ku11.png", width=800)
        st.write("Result of the Topic Modelling with Bertopic:")
        st.image("Analytics_Result/spd/kuehnert/ku12.png", width=800)
        st.image("Analytics_Result/spd/kuehnert/ku13.png", width=800)
        st.image("Analytics_Result/spd/kuehnert/ku14.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>10. Emotion Analysis</h4>",unsafe_allow_html=True)
        st.write("Steps to take to connect tweets with emotions")
        st.write("1. Create a list of words were the emotion of each is entered as a 0 or 1")
        st.write("2. Go threw every tweets and count the the times a word of each emotion appears")
        st.write("3. Save in a new column for each emotion the number of times the emotion appears in the tweet")
        st.write("Show the top 15 words for every emotion: ")
        st.image("Analytics_Result/spd/kuehnert/ku15.png", width=800)
        st.image("Analytics_Result/spd/kuehnert/ku16.png", width=800)
        st.image("Analytics_Result/spd/kuehnert/ku17.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>11. Connect Sentiment and Emotion Analysis for Comparison</h4>",unsafe_allow_html=True)
        st.write("Declare Freude, Vorfreude, Vertrauen and Überraschung as positive emotions.")
        st.write("Declare Traurigkeit, Furcht, Ekel and Wut as negative emotions.")
        st.write("Count the total number of times a negative or positive emotion accurs in a tweet and save the number in two extra columns.")
        st.write("Go threw each tweet and safe in a new column if there are more then 0 total negative or positive emotions.")
        st.write(" ")
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a negative emotion:")
        st.image("Analytics_Result/spd/kuehnert/ku18.png", width=800)
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a positive emotion:")
        st.image("Analytics_Result/spd/kuehnert/ku19.png", width=800)
        st.write("Show the percentage of tweets which share the emotion and sentiment:")
        st.image("Analytics_Result/spd/kuehnert/ku20.png", width=800)
        st.image("Analytics_Result/spd/kuehnert/ku21.png", width=800)        

# Karl Lauterbach

   if optionspd == 'Prof. Dr. Karl Lauterbach':  
        st.write('You selected the politician:', optionspd + ".")
        st.write('Time needed to process data: 13:51,63 min.')
        st.write('Number of tweets: 9492.')
        st.write(" ")
        st.write(" ")
        st.write("<h3 style='text-align: center; color: white;'>Olaf Scholz Twitter Data Analysis</h3>",unsafe_allow_html=True)
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>1. Overview about the number of tweets over time</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/lauterbach/lb1.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>2. Get a first overview over the used words in the tweets.</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/lauterbach/lb2.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>3. Cleaning the text of the dataframe for further processing.</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Changed ÄÜÖäüö to AeUeOEaeueoe")
        st.write("- Saved cleaned data in new column named edited")
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>4. Cleaning the text for sentiment analysis</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Saved cleaned data in new column named textforttb")
        
        st.write("<h4 style='text-align: center; color: white;'>5. Show Wordcloud with cleaned text</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/lauterbach/lb3.png", width=800)
       
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
        st.image("Analytics_Result/spd/lauterbach/lb4.png", width=800)
        st.write("Show the percentage of each polarity as numbers and diagram:")
        st.image("Analytics_Result/spd/lauterbach/lb5.png", width=800)
        st.image("Analytics_Result/spd/lauterbach/lb6.png", width=800)
        st.write("Show the polarity and subjectivty of tweets over time:")
        st.image("Analytics_Result/spd/lauterbach/lb7.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>8. Word related analysis</h4>",unsafe_allow_html=True)
        st.write("Show the amount of words per tweet:")
        st.image("Analytics_Result/spd/lauterbach/lb8.png", width=800)
        st.write("Show a list of the most frequent words:")
        st.image("Analytics_Result/spd/lauterbach/lb9.png", width=800)
        st.write("Show a list of the most frequent trigram ofwords:")
        st.image("Analytics_Result/spd/lauterbach/lb10.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>9. Topic Analysis with LDA and Bertopic</h4>",unsafe_allow_html=True)
        st.write("Result of the LDA analysis:")
        st.image("Analytics_Result/spd/lauterbach/lb11.png", width=800)
        st.write("Result of the Topic Modelling with Bertopic:")
        st.image("Analytics_Result/spd/lauterbach/lb12.png", width=800)
        st.image("Analytics_Result/spd/lauterbach/lb13.png", width=800)
        st.image("Analytics_Result/spd/lauterbach/lb14.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>10. Emotion Analysis</h4>",unsafe_allow_html=True)
        st.write("Steps to take to connect tweets with emotions")
        st.write("1. Create a list of words were the emotion of each is entered as a 0 or 1")
        st.write("2. Go threw every tweets and count the the times a word of each emotion appears")
        st.write("3. Save in a new column for each emotion the number of times the emotion appears in the tweet")
        st.write("Show the top 15 words for every emotion: ")
        st.image("Analytics_Result/spd/lauterbach/lb15.png", width=800)
        st.image("Analytics_Result/spd/lauterbach/lb16.png", width=800)
        st.image("Analytics_Result/spd/lauterbach/lb17.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>11. Connect Sentiment and Emotion Analysis for Comparison</h4>",unsafe_allow_html=True)
        st.write("Declare Freude, Vorfreude, Vertrauen and Überraschung as positive emotions.")
        st.write("Declare Traurigkeit, Furcht, Ekel and Wut as negative emotions.")
        st.write("Count the total number of times a negative or positive emotion accurs in a tweet and save the number in two extra columns.")
        st.write("Go threw each tweet and safe in a new column if there are more then 0 total negative or positive emotions.")
        st.write(" ")
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a negative emotion:")
        st.image("Analytics_Result/spd/lauterbach/lb18.png", width=800)
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a positive emotion:")
        st.image("Analytics_Result/spd/lauterbach/lb19.png", width=800)
        st.write("Show the percentage of tweets which share the emotion and sentiment:")
        st.image("Analytics_Result/spd/lauterbach/lb20.png", width=800)
        st.image("Analytics_Result/spd/lauterbach/lb21.png", width=800)

# Saskia Esken

   if optionspd == 'Saskia Esken':  
        st.write('You selected the politician:', optionspd + ".")
        st.write('Time needed to process data: 1:09:56,83 min.')
        st.write('Number of tweets: 30612.')
        st.write(" ")
        st.write(" ")
        st.write("<h3 style='text-align: center; color: white;'>Olaf Scholz Twitter Data Analysis</h3>",unsafe_allow_html=True)
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>1. Overview about the number of tweets over time</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/esken/ek1.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>2. Get a first overview over the used words in the tweets.</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/esken/ek2.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>3. Cleaning the text of the dataframe for further processing.</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Changed ÄÜÖäüö to AeUeOEaeueoe")
        st.write("- Saved cleaned data in new column named edited")
        st.write(" ")
        
        st.write("<h4 style='text-align: center; color: white;'>4. Cleaning the text for sentiment analysis</h4>",unsafe_allow_html=True)
        st.write("- Removed Mentions, Hashtags, single letters, @ and -")
        st.write("- Saved cleaned data in new column named textforttb")
        
        st.write("<h4 style='text-align: center; color: white;'>5. Show Wordcloud with cleaned text</h4>",unsafe_allow_html=True)
        st.image("Analytics_Result/spd/esken/ek3.png", width=800)
       
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
        st.image("Analytics_Result/spd/esken/ek4.png", width=800)
        st.write("Show the percentage of each polarity as numbers and diagram:")
        st.image("Analytics_Result/spd/esken/ek5.png", width=800)
        st.image("Analytics_Result/spd/esken/ek6.png", width=800)
        st.write("Show the polarity and subjectivty of tweets over time:")
        st.image("Analytics_Result/spd/esken/ek7.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>8. Word related analysis</h4>",unsafe_allow_html=True)
        st.write("Show the amount of words per tweet:")
        st.image("Analytics_Result/spd/esken/ek8.png", width=800)
        st.write("Show a list of the most frequent words:")
        st.image("Analytics_Result/spd/esken/ek9.png", width=800)
        st.write("Show a list of the most frequent trigram ofwords:")
        st.image("Analytics_Result/spd/esken/ek10.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>9. Topic Analysis with LDA and Bertopic</h4>",unsafe_allow_html=True)
        st.write("Result of the LDA analysis:")
        st.image("Analytics_Result/spd/esken/ek11.png", width=800)
        st.write("Result of the Topic Modelling with Bertopic:")
        st.image("Analytics_Result/spd/esken/ek12.png", width=800)
        st.image("Analytics_Result/spd/esken/ek13.png", width=800)
        st.image("Analytics_Result/spd/esken/ek14.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>10. Emotion Analysis</h4>",unsafe_allow_html=True)
        st.write("Steps to take to connect tweets with emotions")
        st.write("1. Create a list of words were the emotion of each is entered as a 0 or 1")
        st.write("2. Go threw every tweets and count the the times a word of each emotion appears")
        st.write("3. Save in a new column for each emotion the number of times the emotion appears in the tweet")
        st.write("Show the top 15 words for every emotion: ")
        st.image("Analytics_Result/spd/esken/ek15.png", width=800)
        st.image("Analytics_Result/spd/esken/ek16.png", width=800)
        st.image("Analytics_Result/spd/esken/ek17.png", width=800)
        
        st.write("<h4 style='text-align: center; color: white;'>11. Connect Sentiment and Emotion Analysis for Comparison</h4>",unsafe_allow_html=True)
        st.write("Declare Freude, Vorfreude, Vertrauen and Überraschung as positive emotions.")
        st.write("Declare Traurigkeit, Furcht, Ekel and Wut as negative emotions.")
        st.write("Count the total number of times a negative or positive emotion accurs in a tweet and save the number in two extra columns.")
        st.write("Go threw each tweet and safe in a new column if there are more then 0 total negative or positive emotions.")
        st.write(" ")
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a negative emotion:")
        st.image("Analytics_Result/spd/esken/ek18.png", width=800)
        st.write("Shows the percentage of tweets with certain sentiment and if the tweet has a positive emotion:")
        st.image("Analytics_Result/spd/esken/ek19.png", width=800)
        st.write("Show the percentage of tweets which share the emotion and sentiment:")
        st.image("Analytics_Result/spd/esken/ek20.png", width=800)
        st.image("Analytics_Result/spd/esken/ek21.png", width=800)        
    
    
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

    
    

