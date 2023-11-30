
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample Documents
documents = [
    "Natural language processing (NLP) is a field of study in artificial intelligence.",
    "NLP techniques are used in various applications like machine translation and sentiment analysis.",
    "The development of NLP tools and libraries has made text analysis easier."
]

# User Query
query = "What is NLP?"

# Combine documents and query for TF-IDF vectorization
corpus = documents + [query]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Calculate cosine similarity between the query and documents
cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

# Sort documents based on cosine similarity
results = [(similarity, documents[i]) for i, similarity in enumerate(cosine_similarities[0])]

# Display the results
results.sort(reverse=True)
for similarity, document in results:
    print(f"Cosine Similarity: {similarity:.4f}\nDocument: {document}\n")