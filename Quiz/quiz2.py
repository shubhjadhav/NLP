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


url = "https://en.wikipedia.org/wiki/Natural_language_processing"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()


def clean_text(sentence):
    words_token = word_tokenize(sentence)
    words_wo_special_char = [word.strip() for word in words_token if word.isalnum() or word in string.punctuation]
    words_wo_stopwords = [word.lower() for word in words_wo_special_char if word.lower() not in stop_words]
    cleaned_tokens = [wnl.lemmatize(word) for word in words_wo_stopwords]
    cleaned_sentence = ' '.join(cleaned_tokens)
    return cleaned_tokens, cleaned_sentence


sentences = sent_tokenize(text)
sentence_features = []

for sentence in sentences:
    cleaned_tokens, cleaned_sentence = clean_text(sentence)
    word_cnt = len(cleaned_tokens)

    pos_tags = pos_tag(cleaned_tokens)
    verb_cnt = len([word for word, pos in pos_tags if pos.startswith('V')])
    noun_cnt = len([word for word, pos in pos_tags if pos.startswith('N')])

    sentence_features.append({
        'sentence': cleaned_sentence,
        'word_cnt': word_cnt,
        'verb_cnt': verb_cnt,
        'noun_cnt': noun_cnt
    })

wiki_df = pd.DataFrame(sentence_features)

print(wiki_df.head())

