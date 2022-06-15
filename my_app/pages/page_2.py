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

optionpp = st.selectbox(
     'Political Party',
     ('AFD', 'CDU/CSU', 'SPD', 'Bündnis90/Die Grünen', 'Die Linke', 'FDP'))

if optionpp=='AFD':
   st.write('You selected the political party:', optionpp)
   optionafd = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('Tino Chrupalla', 'Dr. Alice Weidel', 'Beatrix von Storch', 'Norbert Kleinwächter', 'Leif Erik Holm'))
elif optionpp=='CDU/CSU':
   st.write('You selected the political party:', optionpp)
   optioncducsu = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('Daniela Ludwig', 'Andreas Scheuer', 'Friedrich Merz', 'Philip Amthor', 'Jens Spahn', 'Julia Klöckner', 'Armin Laschet'))
elif optionpp=='SPD':
   st.write('You selected the political party:', optionpp)
   optionspd = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('Olaf Scholz', 'Christine Lambrecht', 'Saskia Esken', 'Kevin Kühnert', 'Prof. Dr. Karl Lauterbach'))
elif optionpp=='Bündnis90/Die Grünen':
   st.write('You selected the political party:', optionpp)
   optiongruenen = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('Renate Künast', 'Annalena Baerbock', 'Katrin Göring-Eckardt', 'Emilia Fester', 'Cem Özdemir'))
elif optionpp=='Die Linke':
   st.write('You selected the political party:', optionpp)
   optionlinke = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('Dr. Dietmar Bartsch', 'Dr. Gregor Gysi', 'Susanne Henning-Wellsow', 'Petra Pau', 'Janine Wissler'))
elif optionpp=='FDP':
   st.write('You selected the political party:', optionpp)
   optionfdp = st.selectbox(
     'Following politicans of this party were analyzed. Pick one to see it!',
     ('Christian Lindner', 'Ulrike Harzer', 'Christian Sauter', 'Dr. Marco Buschmann', 'Volker Wissing'))


