print(50 * '-' + '\n' + 20 * ' ' + 'NLP - Homework 3\n' + 50 * '-')

import nltk
from nltk import word_tokenize, sent_tokenize, Text, FreqDist, pos_tag, PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords, words
from urllib import request
from bs4 import BeautifulSoup

# # ----------------------------------------------------------------
# # HW Q1:
# # In part of this exercise, you will use nltk to explore the Moby Dick text.
# # i. Analyzing Moby Dick text. Load the moby.txt file into python environment. (Load the
# # raw data or Use the NLTK Text object)
# # ii. Tokenize the text into words. How many tokens (words and punctuation symbols) are in it?
# # iii. How many unique tokens (unique words and punctuation) does the text have?
# # iv. After lemmatizing the verbs, how many unique tokens does it have?
# # v. What is the lexical diversity of the given text input?
# # vi. What percentage of tokens is 'whale' or 'Whale'?
# # vii. What are the 20 most frequently occurring (unique) tokens in the text? What is their
# # frequency?
# # viii. What tokens have a length of greater than 6 and frequency of more than 160?
# # ix. Find the longest word in the text and that word’s length.
# # x. What unique words have a frequency of more than 2000? What is their frequency?
# # xi. What is the average number of tokens per sentence?
# # xii. What are the 5 most frequent parts of speech in this text? What is their frequency?
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW3 Q1' + 20 * '-')
#
# f = open('Data/moby.txt')
# raw_text = f.read()
# words_token = word_tokenize(raw_text)
# print(f"\nQ1.2) Number of tokens: {len(words_token)}")
# print(f"\nQ1.3) Number of unique tokens: {len(set(words_token))}")
#
# wnl = WordNetLemmatizer()
# lemmatized_tokens = [wnl.lemmatize(t) for t in words_token]
# print(f"\nQ1.4) Number of unique tokens after lemmatization: {len(set(lemmatized_tokens))}")
#
# lexical_diversity = len(set(words_token)) / len(words_token)
# print(f"\nQ1.5) Lexical diversity: {lexical_diversity:.2f}")
#
# whale_count = words_token.count('whale') + words_token.count('Whale')
# percentage_whale = (whale_count / len(words_token)) * 100
# print(f"\nQ1.6) Percentage of 'whale' or 'Whale': {percentage_whale:.2f}%")
#
# freq_dist = FreqDist(words_token)
# most_common_20 = freq_dist.most_common(20)
# print("\nQ1.7) 20 most frequently occurring (unique) tokens")
# for i, word_freq in enumerate(most_common_20):
#     print(str(i+1) + ': ' + word_freq[0] + ': ' + str(word_freq[1]))
#
# words_gt6_freq_gt160 = [word_freq for word_freq in freq_dist.items() if len(word_freq[0]) > 6 and word_freq[1] > 160]
# print("\nQ1.8) Tokens have a length of greater than 6 and frequency of more than 160")
# for i, word_freq in enumerate(words_gt6_freq_gt160):
#     print(str(i+1) + ': ' + word_freq[0] + ': ' + str(word_freq[1]))
#
# longest_word = max(words_token, key=len)
# print(f"\nQ1.9) The longest word in the text is {longest_word} and its length is {len(longest_word)}")
#
# words_freq_gt2000 = [word_freq for word_freq in freq_dist.items() if word_freq[1] > 2000]
# print("\nQ1.10) Unique words have a frequency of more than 2000")
# for i, word_freq in enumerate(words_freq_gt2000):
#     print(str(i+1) + ': ' + word_freq[0] + ': ' + str(word_freq[1]))
#
# sentences = sent_tokenize(raw_text)
# tokens_sentence = [len(word_tokenize(sentence)) for sentence in sentences]
# print(f"\nQ1.11) Average number of tokens per sentence: {sum(tokens_sentence)/len(tokens_sentence):.2f}")
#
# pos = pos_tag(words_token)
# pos_freq_dist = FreqDist(tag for word, tag in pos)
# most_common_pos = pos_freq_dist.most_common(5)
# print("\nQ1.12) 5 most frequent parts of speech")
# for i, word_freq in enumerate(most_common_pos):
#     print(str(i+1) + ': ' + word_freq[0] + ': ' + str(word_freq[1]))
#
# print('\n' + 20 * '-' + 'End HW3 Q1' + 20 * '-')
#
# # ----------------------------------------------------------------
# # HW Q2:
# # Lets get some text file from the Benjamin Franklin wiki page.
# # i. Write a function that scrape the web page and return the raw text file.
# # ii. Use BeautifulSoup to get text file and clean the html file.
# # iii. Write a function called unknown, which removes any items from this set that occur in the
# # Words Corpus (nltk.corpus.words).
# # iv. Fins a list of novel words.
# # v. Use the porter stemmer to stem all the items in novel words the go through the unknown
# # function, saving the result as novel-stems.
# # vi. Find as many proper names from novel-stems as possible, saving the result as proper names.
# # ----------------------------------------------------------------
# print('\n\n' + 20 * '-' + 'Begin HW3 Q2' + 20 * '-')
#
# url = "https://en.wikipedia.org/wiki/Benjamin_Franklin"
# html = request.urlopen(url).read().decode('utf8')
# bf_raw_text = BeautifulSoup(html, 'html.parser').get_text()
# words_corpus = set(words.words())
# bf_tokens = word_tokenize(bf_raw_text)
#
#
# def unknown(text_tokens):
#     return [word for word in text_tokens if word.lower() not in words_corpus]
#
#
# bf_not_words = unknown(bf_tokens)
# print(f"\nQ2.3) Number of words after removing from Words Corpus: {len(bf_not_words)}")
#
# novel_bf_words = set(bf_not_words)
# print(f"\nQ2.4) Number of novel words: {len(novel_bf_words)}")
#
# stemmer = PorterStemmer()
# novel_stems = [stemmer.stem(word) for word in novel_bf_words]
# print(f"\nQ2.5) Number of novel stems: {len(novel_stems)}")
#
# proper_names = [word for word in novel_stems if word.istitle()]
# print(f"\nQ2.5) Number of proper names: {len(proper_names)}")
#
# print('\n' + 20 * '-' + 'End HW3 Q2' + 20 * '-')
#
# ----------------------------------------------------------------
# HW Q2:
# In part of this exercise, you will use the twitter data.
# i. Load the data and view the first few sentences.
# ii. Split data into sentences using ”\n” as the delimiter.
# iii. Tokenize sentences (split a sentence into a list of words). Convert all tokens into lower
# case so that words which are capitalized
# iv. Split data into training and test sets.
# v. Count how many times each word appears in the data.
# ----------------------------------------------------------------
print('\n\n' + 20 * '-' + 'Begin HW3 Q3' + 20 * '-')

f = open('Data/twitter.txt')
twitter_text = f.read()
tweets = twitter_text.split('\n')

print(f"\nQ3.1) First few sentences:")
for i, tweet in enumerate(tweets[:3]):
    print(f"Tweet {i+1}: {tweet}")

tweets_token = []
for tweet in tweets:
    tweets_token.extend(tweet.lower().split())
print(f"\nQ3.3) Number of tokens: {len(tweets_token)}")

freq_dist = FreqDist(tweets_token)
print(freq_dist)