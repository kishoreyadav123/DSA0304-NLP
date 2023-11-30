

import spacy

def perform_ner(text):
    # Load spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input text
    doc = nlp(text)

    # Extract named entities
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    return entities

# Example text
input_text = "The capital of France is Paris, and it's known for the Eiffel Tower."

# Perform Named Entity Recognition
ner_results = perform_ner(input_text)

# Print the named entities and their labels
for entity, label in ner_results:
    print(f"Entity: {entity}, Label: {label}")