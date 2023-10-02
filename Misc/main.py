import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define the text (replace with your actual text)
text = "Your text goes here. Replace this with the actual text you want to analyze."

# Task 1: Count the number of sentences in the text
doc = nlp(text)
num_sentences = len(list(doc.sents))
print(f"\n1. Number of sentences in the text: {num_sentences}")

# Task 2: Count the number of tokens in the first sentence
first_sentence = list(doc.sents)[0]
num_tokens_first_sentence = len(list(first_sentence))
print(f"\n2. Number of tokens in the first sentence: {num_tokens_first_sentence}")

# Task 3: Get POS tags of tokens in the first sentence and print them in a table
pos_tags_first_sentence = [(token.text, token.pos_) for token in first_sentence]
print("\n3. POS tags of tokens in the first sentence:")
print("Token\tPOS")
for token, pos in pos_tags_first_sentence:
    print(f"{token} -> {pos}")

# Task 4: Count the number of positive adjectives in the text
positive_adjectives = 0
for token in doc:
    if token.pos_ == "ADJ" and token.sentiment > 0:
        positive_adjectives += 1
print(f"\n4. Number of positive adjectives in the text: {positive_adjectives}")

# Task 5: Creative feature - Counting named entities in the text
named_entities = list(doc.ents)
num_named_entities = len(named_entities)
print(f"\n5. Number of named entities in the text: {num_named_entities}")
