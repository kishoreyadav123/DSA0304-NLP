
import spacy

# Load the English model "en_core_web_sm"
nlp = spacy.load("en_core_web_sm")

# Given sentences
sentences = [
    "Apple Inc. is headquartered in Cupertino, California, and its CEO, Tim Cook, often delivers keynote speeches.",
    "The Eiffel Tower in Paris, France, is a popular tourist attraction."
]

# Perform Named Entity Recognition (NER) for each sentence
for sentence in sentences:
    # Process the text using SpaCy
    doc = nlp(sentence)

    # Print named entities and their labels
    print("\nOriginal Sentence:", sentence)
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")