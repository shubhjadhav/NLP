import requests
from bs4 import BeautifulSoup
import pandas as pd
import string

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, pos_tag, sent_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')

wnl = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Scrape text from bulletin
url = "https://bulletin.gwu.edu/university-regulations/#GGrades"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()


def clean_text(text):
    # Tokenize the words in the sentence
    words_token = word_tokenize(text)

    # Remove special characters
    words_wo_special_char = [word.strip() for word in words_token if word.isalnum() or word in string.punctuation]

    # Remove high frequency/stop words
    words_wo_stopwords = [word.lower() for word in words_wo_special_char if word.lower() not in stop_words]

    # Lemmatization
    cleaned_tokens = [wnl.lemmatize(word) for word in words_wo_stopwords]

    return cleaned_tokens


cleaned_tokens = clean_text(text)

# Part of Speech
pos_tags = pos_tag(cleaned_tokens)

features = []

for word in cleaned_tokens:
    char_cnt = len(word)
    is_verb = 1 if nltk.pos_tag([word])[0][1].startswith('V') else 0
    is_noun = 1 if nltk.pos_tag([word])[0][1].startswith('N') else 0
    features.append([word, char_cnt, is_verb, is_noun])

columns = ["word", "char_cnt", "is_verb", "is_noun"]
df = pd.DataFrame(features, columns=columns)

print(df.head())
