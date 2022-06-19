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










