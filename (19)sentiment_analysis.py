
from transformers import pipeline

def analyze_sentiment(text):
    # Load sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")

    # Analyze sentiment
    result = sentiment_pipeline(text)

    return result[0]

# Example text
input_text = "I love this product! It's amazing."

# Perform sentiment analysis
sentiment_result = analyze_sentiment(input_text)

# Print the sentiment and its confidence score
print(f"Sentiment: {sentiment_result['label']}, Confidence: {sentiment_result['score']}")