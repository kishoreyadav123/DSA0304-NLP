import spacy

# Load the SpaCy English NLP model
nlp = spacy.load("en_core_web_sm")

# Given sentence
sentence = "Barack Obama was the 44th President of the United States, and he was born in Honolulu, Hawaii."

# Process the text with SpaCy
doc = nlp(sentence)

# Extract and print named entities
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text}: {ent.label_}")