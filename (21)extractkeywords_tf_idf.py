from sklearn.feature_extraction.text import TfidfVectorizer

# Given sentences
sentences = [
    "Artificial intelligence (AI) is a field of computer science.",
    "Machine learning is a subset of AI that focuses on training models to make predictions.",
    "Deep learning is a type of machine learning that uses neural networks with multiple layers.",
    "Neural networks are composed of interconnected nodes called neurons.",
    "Recurrent neural networks (RNNs) are commonly used in natural language processing tasks.",
]

# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the sentences
tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)

# Get feature names (words) from the vectorizer
feature_names = tfidf_vectorizer.get_feature_names_out()

# Identify key phrases by finding words with high TF-IDF scores in each sentence
key_phrases = []
for i, sentence in enumerate(sentences):
    scores = tfidf_matrix[i].toarray().flatten()
    # Get indices of top TF-IDF scores
    top_indices = scores.argsort()[-3:][::-1]
    # Get corresponding words from feature names
    top_words = [feature_names[idx] for idx in top_indices]
    key_phrases.append(top_words)

# Print the identified key phrases for each sentence
for i, key_phrase in enumerate(key_phrases):
    print(f"Sentence {i + 1}: Key Phrases - {', '.join(key_phrase)}")