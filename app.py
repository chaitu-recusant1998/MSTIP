import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
#from nltk.tokenize import word_tokenize



def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return ' '.join(y)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('Email Spam Classifer')

input_mail = st.text_input('Enter the Email Message to be classified')


if st.button('Predict'):

    # 1. Preprocess
    transformed_mail = transform_text(input_mail)
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_mail])
    # 3. Predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header('It is a spam message')
    else:
        st.header('It is not a spam message. Read it carefully!')

