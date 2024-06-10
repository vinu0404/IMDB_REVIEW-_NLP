import streamlit as st
import pickle


import nltk
import re
import nltk.stem.porter


from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
from nltk.corpus import stopwords
stopwords.words("english")
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def transform_text(text):
    text=text.lower()

    text=nltk.word_tokenize(text)
    
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
      

    text=y[:]
    y.clear()

    for i in text:
        if i  not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)
    

vector=pickle.load(open("vect.pkl","rb"))
model=pickle.load(open("modell.pkl","rb"))

st.title("Review Analysis of Fans")
input_rev=st.text_area("Enter your Review")
if st.button("Check Review"):

        #preprocess
        transform_rev=transform_text(input_rev)
        print(transform_rev)

        count_vector=vector.transform([transform_rev])

        result=model.predict(count_vector)[0]

        if result ==1:
            st.header("LIKED 🙂 ")
        else:
            st.header("NOT LIKED 😐")



