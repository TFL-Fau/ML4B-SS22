import streamlit as st
import pandas as pd
import joblib
#import pickle


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

st.write("<h1 style='text-align: center;'>Algorithm Live Demo</h1>",unsafe_allow_html=True)

with st.expander("Before you start...", expanded=False):

    st.write("<h4 style='text-align: center;'>Introduction to Live Demo:</h4>",unsafe_allow_html=True)
    st.write('The Model used in this case was trained on 5000 Tweets of Saskia Esken. Accordingly the results have the highest quality when trying to recognise the emotions of Saskia Eskens tweets.')
    st.write('Here are a few Tweets of hers, that were not part of the training data set (due to them being very recent) that you can try for yourself.')
    st.write('- https://twitter.com/EskenSaskia/status/1540694896054370306')
    st.write('- https://twitter.com/EskenSaskia/status/1540329983553552386')
    st.write('- https://twitter.com/EskenSaskia/status/1539314052723200000')
    st.write('- https://twitter.com/EskenSaskia/status/1534638331904118791')
    st.write('This model could and should be expanded in the future by just training the model on a greater training set with mixed tweets of multiple politicians. But while it is only trained on a single politician it provides its best use at recognising the emotion of tweets, that that politician is writing.')
    
    

sentence = st.text_input('Please enter a sentence to analyse it on emotions:', '')




# Code for analysis

import re

def clean(text):
    text = re.sub(r'@[A-Za-z0-9]+\s?', '', text) #Removed Mentions
    text = re.sub(r'#', '', text) #Removed #
    text = re.sub(r'(.)1+', r'1', text) #cleaned single letters
    text = re.sub('((www.[^s]+)|(https?://[^s]+))','',text) #Removes links
    text = re.sub('@','',text) #Remove @
    text = re.sub('-','',text) #Remove -
    text = re.sub(r'[^\w\s]', '', text) # Remove punctations
    text = re.sub('ä','ae',text) #Remove ä
    text = re.sub('Ä','Ae',text) #Remove Ä
    text = re.sub('ö','oe',text) #Remove Ä
    text = re.sub('Ö','Oe',text) #Remove Ä
    text = re.sub('ü','ue',text) #Remove Ä
    text = re.sub('Ü','Ue',text) #Remove Ä
    return text

import nltk
from nltk.stem import PorterStemmer
porter = PorterStemmer()
sp = nltk.PorterStemmer()
def stemming_on_text(data):
    text = [sp.stem(word) for word in data]
    return data

def sentence_toVec(sentence,goalDF):
    #Preparing Input text
    cleanSentence = sentence.lower()
    cleanSentence = clean(cleanSentence)
    cleansentene = stemming_on_text(cleanSentence)
    
    #Preparing EmptyDF
    emptyList = [0]*len(goalDF.keys())
    #print(emptyList)
    #print("Len EmptyList: " + str(len(emptyList)))
    #emptyDF = goalDF.iloc[0:0].copy()
    #emptyDF = emptyDF.append(emptyList)
    #emptyDF = emptyDF.append(pd.DataFrame(emptyList, columns = goalDF.keys()), ignore_index = True)
    emptyDF = pd.DataFrame(columns = goalDF.keys())
    #emptyDF.append(pd.Series(), ignore_index = True)
    emptyDF.loc[len(emptyDF)] = emptyList
    #print(emptyDF)
    #emptyDF = pd.DataFrame(emptyList, columns = goalDF.keys())
    #print("LenEmpty DF: " + str(len(emptyDF)) + " Len Keys Empty DF: " + str(len(emptyDF.keys())))
    
    emptyDF["textInput"][0] = sentence
    emptyDF["editedInput"][0] = cleanSentence
    #keys = list(emptyDF.keys()[0:10])
    #print("---")
    #print("New LenEmpty DF: " + str(len(emptyDF)) + " Len Keys Empty DF: " + str(len(emptyDF.keys())))
    #print(emptyDF["textInput"].tolist())
    listOfWords = cleanSentence.split()
    for word in listOfWords:
        if word in emptyDF.columns:
            emptyDF[word][0] = 1
    emptyDF.fillna(0)
    return emptyDF

def getAttributesOfTweet(tweetNumber, df):
    keys = list(df.keys()[12:20])
    #st.write("---\n Tweet\n---\n" + df["textInput"][tweetNumber]+"\n---")
    st.write("---\n")
    st.write('Your entered sentence is:')
    st.write(sentence)
    stringOfEmotion = ""
    stringOfNotEmotion = ""
    countEmotionsActive = 0
    countEmotionsPassive = 0
    for emotion in df[keys]:
        emotionText = emotion[:-5]
        if(emotionText == "Ueberraschung"):
            emotionText="Überraschung"
        if(1==df[emotion][tweetNumber]):
            if(len(stringOfEmotion)>0):
                stringOfEmotion = stringOfEmotion +", "
            stringOfEmotion = stringOfEmotion + emotionText
            countEmotionsActive = countEmotionsActive + 1
        else:
            if(len(stringOfNotEmotion)>0):
                stringOfNotEmotion = stringOfNotEmotion +", "
            stringOfNotEmotion = stringOfNotEmotion + emotionText
            countEmotionsPassive = countEmotionsPassive + 1
    if(countEmotionsActive > 1):
        st.markdown("The algorithm determined the emotions <u><b>" + stringOfEmotion +"</b></u> in the tweet based on the training.")
    elif(countEmotionsActive == 1):
        st.markdown("The algorithm determined the emotion __**" + stringOfEmotion +"**__  in the tweet based on the training.")
    else:
        st.markdown("The algorithm did not detect any emotions in the tweet based on the training.")
    
    if(countEmotionsPassive > 1):
        st.markdown("Thus, the emotions __**" + stringOfNotEmotion+ "**__ according to the algorithm, are not included in the tweet.")
    elif(countEmotionsPassive == 1):     
        st.markdown("Thus, the emotion __**" + stringOfNotEmotion+ "**__ according to the algorithm, is not included in the tweet.")
    else:
        st.markdown("As a result, all emotions known to the algorithm are included in the tweet.")

def interpretOwnSentence(sentence, dicOfModels, df):
    if(len(sentence) == 0):
        return
    if(type(sentence) != str):
        st.write("Sentence-Parameter is not a String.")
        return
    if(type(dicOfModels) != dict):
        st.write("dicOfModels-Parameter is not a dictionary.")
        return
    if(len(dicOfModels)!=8):
        st.write("dicOfModels Length is not 8.")
        return
    #st.write('Your entered sentence is: ', sentence)
        
    #Transforming Sentence into Vector
    dfOfSentence = sentence_toVec(sentence, df)
    #print("----\nThis is the shape of the df: \n" + str(dfOfSentence) + "\n----")
    listOfIndex = dfOfSentence.columns[(dfOfSentence == 1).all()].tolist()
    listOfIndex.extend(["textInput","editedInput","WutInput"])
    #print("----\nInput Sentence was transformed to this vector: \n" +str(dfOfSentence.head()))
    keys = list(df.keys()[12:20])
    #Applying different Models to sentences
    keyOfFeatures = dfOfSentence.keys()[24:]
    features = dfOfSentence[keyOfFeatures]    
    iterator = 0
    for model in dicOfModels:
        #print(str(model) + " is the following type: " + str(type(model)))
        result = dicOfModels[model].predict(features)
        #print("---\nThis is the result of {}: ".format(str(model)) + str(result))
        #print("result[0]: " + str(result[0]))
        #print("before writing: " + str(dfOfSentence[dfOfSentence.keys()[12+iterator]]))
        #dfOfSentence[12+iterator] = result[0]
        dfOfSentence[dfOfSentence.keys()[12+iterator]][0] = result[0]
        #print(dfOfSentence[dfOfSentence.keys()[12+iterator]][0])
        #print("---\nThis is in the dfOfSentence: " + str(dfOfSentence[12+iterator][0]))
        if(dfOfSentence[dfOfSentence.keys()[12+iterator]][0]>1):
            dfOfSentence[dfOfSentence.keys()[12+iterator]][0] = 1
        iterator = iterator + 1
    #print("---\nThis is what all the Attributes look like: \n" + str(dfOfSentence[dfOfSentence.keys()[12:20]]))
    getAttributesOfTweet(0,dfOfSentence)


vd = pd.read_csv("my_app/vectorizedDataframesmall")

vd.drop(["Unnamed: 0"],axis = 1, inplace = True)

filename = 'my_app/finalized_model.sav'
loaded_model = joblib.load(filename) 

#loaded_model = pickle.load(open(filename, 'rb'))

interpretOwnSentence(sentence, loaded_model, vd)