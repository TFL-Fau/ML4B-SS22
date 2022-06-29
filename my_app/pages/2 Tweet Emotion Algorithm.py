import streamlit as st

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

st.write("<h1 style='text-align: center;'>Tweet Emotion Algorithm</h1>",unsafe_allow_html=True)

st.write("<h3 style='text-align: center;'>1. Training our algorithm.</h3>",unsafe_allow_html=True)

st.write("To accomplish an algorithm that is able to detect emotions in tweets, we used a Decision Tree Regressor algorithm. This algorithm got trained on the basis of our data understanding during 'analysis of tweets' where already existing tweets were judged on their emotional context. With the help of CountVectorisation each tweet was discected and was given to the algorithm as training data, with the goal of recognizing individual emotions within the sentence. Due to processing limitation the model was only trained on 5000 tweets of Saskia Esken, which leads to limitiations for emotion recognition, due to limited amount of vocabulary and diversity. This trainingset needs to be extended in future research with more processing power.")

st.write("<h4 style='text-align: center;'>Before we started...</h4>",unsafe_allow_html=True)

st.write("- Extracted the data of two politicians with the biggest datasets")
st.write("- As an result we now got 50.000 tweets with all emotion and sentiment analysis data to train our algorithm")
st.write("- Turned the dataset into Vectors for later Machine Learning")
st.write("- Created our bag of words")

st.write("<h4 style='text-align: center;'>1. Training our algorithm.</h4>",unsafe_allow_html=True)
st.write("- We used 5000 tweets as our training data for our machine learning algorithm")
st.write("- The algorithm we used was an DecisionTreeRegressor")
st.write("More tweets for training were not possible because of our Prozessor and RAM capacity:")
st.image("Algo_Result/algotraining.png", width=800)

st.write("<h4 style='text-align: center;'>2. Explanations</h4>",unsafe_allow_html=True)
st.write("In the following you can see explanations for the Mean Absolute Error, Confusion Matrix, Accuracy, Precision, Recall and f1-Score we used to show our results for every emotion trained:")
st.write("Explanations: ")
st.write("- Mean Absolute Error: Mean Absolute Error (MAE) is calculated by taking the summation of the absolute difference between the actual and calculated values of each observation over the entire array and then dividing the sum obtained by the number of observations in the array")
st.write("- Confusion Matrix: A confusion matrix is a summary of prediction results on a classification problem. The number of correct and incorrect predictions are summarized with count values and broken down by each class. This is the key to the confusion matrix.")
st.write("- Accuracy: Accuracy means the state of being correct or precise, (TP+TN) / (TP + TN + FP + FN)")
st.write("- Precision: Precision (also called positive predictive value) is the fraction of relevant instances among the retrieved instances, (TP+TN) / (TP + TN + FP + FN)")
st.write("- Recall: Recall (also known as sensitivity) is the fraction of relevant instances that were retrieved, TP/(TP+FP)")
st.write("- F1-Score: A measure that combines precision and recall is the harmonic mean of Precision and Recall, (2 * TP) / (2 * TP + FP + FN)")

st.write("<h4 style='text-align: center;'>3. Our Results</h4>",unsafe_allow_html=True)
st.write("In the following you can see the Results in form of the Mean Absolute Error, Confusion Matrix, Accuracy, Precision, Recall and F1-Score for every emotion we trained our model:")
st.image("Algo_Result/r1.png", width=800)
st.image("Algo_Result/r2.png", width=800)
st.image("Algo_Result/r3.png", width=800)
st.image("Algo_Result/r4.png", width=800)
st.image("Algo_Result/r5.png", width=800)
st.image("Algo_Result/r6.png", width=800)
st.image("Algo_Result/r7.png", width=800)
st.image("Algo_Result/r8.png", width=800)

st.write("<h4 style='text-align: center;'>4. Comparing different Machine Learning Algorithms for our case</h4>",unsafe_allow_html=True)

st.write("We also compared the results of 7 different Machine Learning Methods to find out which is best for our use case.")
st.write("We used: ")
st.write("- LR: LogisticRegression")
st.write("- LDA: LinearDiscriminantAnalysis")
st.write("- KNN: KNeighborsClassifier")
st.write("- CART: DecisionTreeClassifier")
st.write("- NB: GaussianNB")
st.write("- SVM: Support Vector Machines")
st.write("- DTR: DecisionTreeRegressor")

st.write("This is our result comparing the predicitions for the emotion Anger (Wut):")
st.image("Algo_Result/comparison.png", width=800)
st.write("The boxplot is useful to shows the most important robust position and dispersion measures.")
st.write("- The orange line is the median")
st.write("- The box shows the higher and lower quartile")
st.write("- The blackline on the bottom and the topic shows the maximum and minimum")
st.write(" ")
st.write("Result of Comparison: The DecisionTreeClassifier algorithm gives us the best predicitions with the highest median score, highest minimum and highest maximum!")

st.write("<h4 style='text-align: center;'>5. Limitations and Further possible Research</h4>",unsafe_allow_html=True)

st.write("Limitations: ")
st.write("- The Training data was automatically flagged for emotions with the help of a emotion word list. As a result of this, words have not been put into relation to other words in the same sentence. This results in the training data not being as precise as it would be, if text was flagged by hand.")
st.write("- This Model was trained on a Limited amount of Tweets and vocabulary of certain politicians. This leads to the Model being limited in the vocabulary and the context that the politician used the tweets in.")
st.write("- As a further result of being trained on a limited amount of Tweets, certain words might have been used in a limited amount of context. An example for this is herzlichen which normaly would be associated positively, but is flagged as Freude, Traurig, Vertrauen. This can result in certain posts having the emotion Sadness, although its a positive tweet")
st.write("- Comparison of differen ML-Models is on a very limited Dataset of 1000 tweets due to lack of computation power. This results in the quality of the different model maybe varying when having a different size of data set.")
st.write("- This results in the Model best being used to analyse the tweet of the politician that the model was trained on. That offers a higher chance of the politician using the same vocabulary in a similiar context.")

st.write("Further possible Research:")

st.write("- Improving the initial emotion recognition input for higher quality / more precise training dataset")
st.write("- Add further politicians for higher veriety and more data")
st.write("- Training a model on normal sentences, to increase the vocabulary and context to allow higher quality of emotion recognition on normal text instead of the specialized format of tweets.")
st.write("- Training the model on bigger tweet dataset than 5000 Tweets")
st.write("- Test if CART Model is realy the supperior ML-Model on a bigger Dataset than the currently implemented DTR Model")

st.write("<h4 style='text-align: center;'>6. Important to Know</h4>",unsafe_allow_html=True)

st.write("- Of course, the results depend on what words the author of the trained tweets uses")
st.write("- A higher number of tweets trained give better predicition scores")















