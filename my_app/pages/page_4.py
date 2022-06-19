import streamlit as st
import pandas as pd
import joblib

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

sentence = st.text_input('Please enter a sentence to analyse it on emotions:', '')
st.write('Your entered sentence is: ', sentence)



# Code for analysis

import re

def clean(text):
    text = re.sub(r'@[A-Za-z0-9]+\s?', '', text) #Removed Mentions
    text = re.sub(r'#', '', text) #Removed #
    text = re.sub(r'(.)1+', r'1', text) #cleaned single letters
    text = re.sub('((www.[^s]+)|(https?://[^s]+))','',text) #Removes links
    text = re.sub('@','',text) #Remove @
    text = re.sub('-','',text) #Remove -
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
st = nltk.PorterStemmer()
def stemming_on_text(data):
    text = [st.stem(word) for word in data]
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

def interpretOwnSentence(sentence, dicOfModels, df):
    if(type(sentence) != str):
        print("Sentence-Parameter is not a String")
        return
    if(type(dicOfModels) != dict):
        print("dicOfModels-Parameter is not a dictionary")
        return
    if(len(dicOfModels)!=8):
        print("dicOfModels Length is not 8")
        return
        
    #Transforming Sentence into Vector
    dfOfSentence = sentence_toVec(sentence, df)
    #print("----\nThis is the shape of the df: \n" + str(dfOfSentence) + "\n----")
    listOfIndex = dfOfSentence.columns[(dfOfSentence == 1).all()].tolist()
    listOfIndex.extend(["textInput","editedInput","WutInput"])
    #print("----\nInput Sentence was transformed to this vector: \n" +str(dfOfSentence.head()))
    keys = list(df.keys()[12:20])
    #Applying different Models to sentence
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


vd = pd.read_csv("vectorizedDataframesmall")
loaded_model = joblib.load('emotionmodel.sav') 

interpretOwnSentence(sentence, loaded_model, vd)










