
import spacy

# Load the English model "en_core_web_sm"
nlp = spacy.load("en_core_web_sm")

# Given sentences
sentences = ["The cat sat on the mat.", "She quickly ran to catch the bus."]

# Perform dependency parsing for each sentence
for sentence in sentences:
    # Process the text using SpaCy
    doc = nlp(sentence)

    # Print the token dependencies
    print("\nOriginal Sentence:", sentence)
    for token in doc:
        print(f"{token.text} --({token.dep_})--> {token.head.text}")