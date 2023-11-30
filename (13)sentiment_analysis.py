pip install textblob

from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Get the sentiment polarity
    polarity = blob.sentiment.polarity

    # Classify the sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example sentences
sentence1 = "I love this product! It's amazing."
sentence2 = "The weather is terrible today."

# Analyze sentiment for each sentence
result1 = analyze_sentiment(sentence1)
result2 = analyze_sentiment(sentence2)

# Print results
print(f"Sentence 1: {result1}")
print(f"Sentence 2: {result2}")