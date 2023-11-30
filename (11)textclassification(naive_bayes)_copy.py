import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# Sample data: Text documents and their corresponding categories
documents = [
    {'text': 'This is a positive document', 'label': 'positive'},
    {'text': 'Negative sentiment in this one', 'label': 'negative'},
    {'text': 'Spam! You won a prize!', 'label': 'spam'},
    {'text': 'Another positive example', 'label': 'positive'},
    {'text': 'More negative text for testing', 'label': 'negative'},
    {'text': 'Congratulations! You are selected as a winner!', 'label': 'spam'},
    # Add more documents as needed
]

# Extract text and labels from the documents
texts = [doc['text'] for doc in documents]
labels = [doc['label'] for doc in documents]

# Split the data into training and testing sets
text_train, text_test, label_train, label_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Vectorize the text using the Bag-of-Words model
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(text_train)
X_test = vectorizer.transform(text_test)

# Train a Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, label_train)

# Make predictions on the test set
predictions = classifier.predict(X_test)

# Print classification metrics
print("Classification Report:")
print(metrics.classification_report(label_test, predictions))
print("\nConfusion Matrix:")
print(metrics.confusion_matrix(label_test, predictions))