import spacy
nlp = spacy.load("en_core_web_sm")
# -----------------------------------------------------------------------------------------
text = """SpaCy is a free, open-source library for advanced Natural Language Processing 
(NLP) in Python. If you're working with a lot of text, you'll eventually want to know 
more about it. For example, what's it about? What do the words mean in context? 
Who is doing what to whom? What companies and products are mentioned?
 Which texts are similar to each other?
SpaCy helps you answer these questions with a powerful, streamlined API that's easy 
to use and integrates seamlessly with other Python libraries. SpaCy also comes with 
pre-trained statistical models and word vectors, and supports deep learning workflows 
that allow you to train and update neural network models on your own data."""
# -----------------------------------------------------------------------------------------
# 1:
# Your code here
doc = nlp(text)
sentences = list(doc.sents)
num_sentences = len(sentences)
print(f"Number of sentences: {num_sentences}")





# -----------------------------------------------------------------------------------------
# 2
# Your code here
first_sentence = sentences[0]
num_tokens_first_sentence = len(list(first_sentence))
print(f"Number of tokens in the first sentence: {num_tokens_first_sentence}")




# -----------------------------------------------------------------------------------------
#3
# Your code here
pos_tags_first_sentence = [(token.text, token.pos_) for token in first_sentence]
print("\nPOS tags of tokens in the first sentence:")
for token, pos in pos_tags_first_sentence:
    print(f"Token: {token}\tPOS: {pos}")




# -----------------------------------------------------------------------------------------
#4
# Your code here
positive_adjectives = [token for token in doc if token.sentiment > 0]
num_positive_adjectives = len(positive_adjectives)
print(f"\nNumber of positive adjectives: {num_positive_adjectives}")




# -----------------------------------------------------------------------------------------
#5
# Your code here
named_entities = [ent.text for ent in doc.ents]
num_named_entities = len(named_entities)
print(f"\nNumber of named entities: {num_named_entities}")