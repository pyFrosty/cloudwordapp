import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from fileupload import FileUpload

st.title('Webapp')

uploaded_file = FileUpload()

text = uploaded_file.read()

stopwords = list(STOPWORDS)
include_stopwords = st.checkbox('Include common stopwords')

if not include_stopwords:
  stopwords.extend(['the','and','to','of','a','in','is','it'])

wc = WordCloud(background_color="white", stopwords=stopwords,max_words=50, colormap='viridis')
wc.generate(text)

frequent_words = Counter(text.split()).most_common(50)
st.write("Top 50 words:")
st.table(frequent_words)

additional_stopwords = st.text_input('Enter additional stopwords').split(',')
stopwords.extend(additional_stopwords)

wc = WordCloud(background_color="white", stopwords=stopwords,max_words=50, colormap='viridis')
fig, ax = plt.subplots()
ax.imshow(wc)
st.pyplot(fig)

st.header('Connect with me!')
st.write('Find me on:')
st.markdown("[LinkedIn](https://www.linkedin.com)")
st.markdown("[GitHub](https://www.github.com)")
