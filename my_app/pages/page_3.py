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

st.write("<h1 style='text-align: center;'>Tweet Emotion Algorithm</h1>",unsafe_allow_html=True)

st.write("- Extracted the data of two politicians with the biggest datasets")
st.write("- As an result we now got 50.000 tweets with all emotion and sentiment analysis data to train our algorithm")
st.write("- Turned the dataset into Vectors for later Machine Learning")
st.write("- Created our bag of words")

st.write("<h4 style='text-align: center;'>1. Training our algorithm.</h4>",unsafe_allow_html=True)
st.write("- We used 5000 tweets as our training data for our machine learning algorithm")
st.write("More was not possible because of our Prozessor and RAM capacity:")
st.image("Algo_Result/algotraining.png", width=800)

