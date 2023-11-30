
import nltk

# Download the necessary NLTK data
nltk.download('punkt')

# Define the CFG rules
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
Det -> 'the'
N -> 'cat' | 'mouse'
VP -> V NP
V -> 'chased'
""")

# Create a ChartParser with the CFG
parser = nltk.ChartParser(grammar)

# Define the sentence as a list of lowercase words
sentence = ["the", "cat", "chased", "the", "mouse"]

# Parse the sentence
for tree in parser.parse(sentence):
    tree.pretty_print()