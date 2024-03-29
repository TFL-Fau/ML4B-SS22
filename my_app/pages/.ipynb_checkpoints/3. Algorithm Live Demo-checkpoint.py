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
    print("---\nTweet \n--- \n" + df["textInput"][tweetNumber]+"\n---")
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
        print("Der Algorithmus hat anhand des Trainings die Emotionen " + stringOfEmotion +" im Tweet ermittelt.")
    elif(countEmotionsActive == 1):
        print("Der Algorithmus hat anhand des Trainings die Emotion " + stringOfEmotion +" im Tweet ermittelt.")
    else:
        print("Der Algorithmus hat anhand des Trainings keine Emotionen im Tweet ermittelt.")
    
    if(countEmotionsPassive > 1):
        print("Dadurch sind die Emotionen " + stringOfNotEmotion+ ", laut dem Algorithmus, nicht im Tweet enthalten.")
    elif(countEmotionsPassive == 1):     
        print("Dadurch ist die Emotion " + stringOfNotEmotion+ ", laut dem Algorithmus, nicht im Tweet enthalten.")
    else:
        print("Dadurch sind alle Emotionen, die dem Algorithmus bekannt sind, im Tweet enthalten.")

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