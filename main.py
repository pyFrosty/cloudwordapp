import streamlit as st
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Set Streamlit app title
st.title("Word Cloud Generator")

# Ask the user to upload a file
file = st.file_uploader("Upload a document (PDF, DOCX, or other formats)")

# Checkbox to remove stop words from the word cloud
remove_stopwords = st.checkbox("Remove Common Stop Words")

# Allow the user to add custom stop words
custom_stopwords = st.text_area("Add additional stop words (comma-separated)", help="e.g., and, the, in")

# Function to generate word cloud
def generate_word_cloud(text, stopwords=None):
    if remove_stopwords and stopwords:
        wordcloud = WordCloud(stopwords=stopwords, width=800, height=400, background_color="white").generate(text)
    else:
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    return wordcloud

# Function to display word frequencies in a table
def display_word_frequencies(text):
    words = text.split()
    word_count = Counter(words)
    word_freq_df = pd.DataFrame(word_count.most_common(50), columns=["Word", "Frequency"])
    st.subheader("Top 50 Words and Frequencies")
    st.write(word_freq_df)

# Function to remove custom stop words
def remove_custom_stopwords(text, custom_stopwords):
    if custom_stopwords:
        custom_stopwords_list = [word.strip() for word in custom_stopwords.split(',')]
        for stopword in custom_stopwords_list:
            text = text.replace(stopword, '')
    return text

if file is not None:
    # Read the uploaded file
    file_contents = file.read()
    
    # Decode bytes to text
    if isinstance(file_contents, bytes):
        file_contents = file_contents.decode('utf-8', 'ignore')
    
    # Remove custom stop words
    file_contents = remove_custom_stopwords(file_contents, custom_stopwords)

    # Generate word cloud
    wordcloud = generate_word_cloud(file_contents, custom_stopwords.split(','))

    # Display Word Cloud
    st.subheader("Word Cloud")
    st.image(wordcloud.to_array(), use_column_width=True)

    # Display word frequencies
    display_word_frequencies(file_contents)

# Section to add social media accounts
st.sidebar.header("Add Your Social Media Accounts")
facebook = st.sidebar.text_input("Facebook:")
twitter = st.sidebar.text_input("Twitter:")
linkedin = st.sidebar.text_input("LinkedIn:")
instagram = st.sidebar.text_input("Instagram:")

# Show the entered social media accounts
st.sidebar.subheader("Your Social Media Accounts:")
st.sidebar.write(f"Facebook: {facebook}")
st.sidebar.write(f"Twitter: {twitter}")
st.sidebar.write(f"LinkedIn: {linkedin}")
st.sidebar.write(f"Instagram: {instagram}")

# You can access the entered social media accounts by using the respective variables (facebook, twitter, linkedin, instagram).

# Make sure to adjust the appearance and styling of the app as desired.
