# =================================================================
# Quiz 2 - Bonus
# =================================================================

import spacy
nlp = spacy.load("en_core_web_sm")

# ----------------------------------------------------------------
# Class_Ex4:
# Use the following sentence as a sample text. and Answer the following questions.
# "In 2020, more than 15% of people in World got sick from a pandemic ( www.google.com ). Now it is less than 1% are. Reference ( www.yahoo.com )"
# 1- Check if there is a token resemble a number.
# 2- Find a percentage in the text.
# 3- How many url is in the text.
# ----------------------------------------------------------------

print(20 * '-' + 'Begin Q1' + 20 * '-')

text = "In 2020, more than 15% of people in World got sick from a pandemic ( www.google.com ). Now it is less than 1% are. Reference ( www.yahoo.com )"

doc = nlp(text)

has_number = any(token.like_num for token in doc)
print(f"1- Token resembling a number: {has_number}")

percentages = [token.text for token in doc if "%" in token.text]
print(f"2- Percentages in the text: {percentages}")

urls = [token.text for token in doc if token.like_url]
print(f"3- Number of URLs in the text: {len(urls)}")

print(20 * '-' + 'End Q1' + 20 * '-')

# =================================================================
# Class_Ex5:
# Load small web english model into spaCy.
# USe the following text as a sample text. Answer the following questions
# "It is shown that: Google was not the first search engine in U.S. tec company. The value of google is 100 billion dollar"
# 1- Get the token text, part-of-speech tag and dependency label.
# 2- Print them in a tabular format.
# ----------------------------------------------------------------
print('\n\n' + 20 * '-' + 'Begin Q2' + 20 * '-')

text = "It is shown that: Google was not the first search engine in U.S. tech company. The value of Google is 100 billion dollars"

doc = nlp(text)

token_info = [(token.text, token.pos_, token.dep_) for token in doc]

print("{:<15} {:<10} {:<15}".format("Token", "POS Tag", "Dependency Label"))
print("="*40)
for token, pos_tag, dep_label in token_info:
    print("{:<15} {:<10} {:<15}".format(token, pos_tag, dep_label))

print(20 * '-' + 'End Q2' + 20 * '-')