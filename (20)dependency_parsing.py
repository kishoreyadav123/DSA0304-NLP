
import spacy

def dependency_parsing(sentence):
    # Load spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input sentence
    doc = nlp(sentence)

    # Extract dependency relations
    dependencies = [(token.text, token.dep_, token.head.text) for token in doc]

    return dependencies

# Example sentences
sentence1 = "John and Mary went to the store."
sentence2 = "The big brown dog chased the small black cat."

# Perform dependency parsing for each sentence
dependencies1 = dependency_parsing(sentence1)
dependencies2 = dependency_parsing(sentence2)

# Print the results
print("Dependencies for Sentence 1:")
for dep in dependencies1:
    print(f"{dep[0]} - {dep[1]} - {dep[2]}")

print("\nDependencies for Sentence 2:")
for dep in dependencies2:
    print(f"{dep[0]} - {dep[1]} - {dep[2]}")