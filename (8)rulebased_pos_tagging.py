
import re

def rule_based_pos_tagging(sentence):
    patterns = [
        (r'\b(?:The|the)\b', 'DET'),         # Matches 'The' or 'the' as determiners
        (r'\b(?:cat|dog)\b', 'NOUN'),         # Matches 'cat' or 'dog' as nouns
        (r'\b(?:is|am|are)\b', 'VERB'),      # Matches 'is,' 'am,' or 'are' as verbs
        (r'\b(?:quickly|brightly)\b', 'ADV'),# Matches 'quickly' or 'brightly' as adverbs
        (r'\b(?:[A-Za-z]+)\b', 'NOUN')       # Matches any other words as nouns
    ]

    tagged_words = []

    for word, pos_tag in patterns:
        matches = re.findall(word, sentence, flags=re.IGNORECASE)
        if matches:
            tagged_words.extend([(match, pos_tag) for match in matches])

    return tagged_words

# Example usage
sentences = [
    "The quick brown fox is running",
    "The dog is barking loudly",
    "She is quickly reading a book"
]

for sentence in sentences:
    tagged_words = rule_based_pos_tagging(sentence)
    print(f"Original Sentence: {sentence}")
    print("Rule-Based POS Tagging:", tagged_words)
    print()