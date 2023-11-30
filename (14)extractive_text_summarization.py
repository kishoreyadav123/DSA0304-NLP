
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

nltk.download('punkt')
nltk.download('stopwords')

def extractive_summarization(document, num_sentences=3):
    # Step 1: Sentence Tokenization
    sentences = sent_tokenize(document)

    # Step 2: Text Preprocessing
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for sentence in sentences for word in nltk.word_tokenize(sentence) if word.isalnum() and word.lower() not in stop_words]

    # Step 3: Calculate Sentence Scores
    word_freq = FreqDist(words)
    sentence_scores = {sentence: sum(word_freq[word] for word in nltk.word_tokenize(sentence) if word.isalnum() and word.lower() not in stop_words) for sentence in sentences}

    # Step 4: Select Top Sentences
    top_sentences = sorted(sentences, key=lambda sentence: sentence_scores[sentence], reverse=True)[:num_sentences]

    # Detokenize to form the final summary
    summary = TreebankWordDetokenizer().detokenize(top_sentences)

    return summary

document = """
Natural language processing (NLP) is a subfield of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. NLP technologies are used to process, analyze, and understand large amounts of natural language data.

One of the primary applications of NLP is sentiment analysis, which determines the sentiment or emotional tone of a piece of text. Sentiment analysis is widely used in social media monitoring, customer feedback analysis, and brand reputation management.

Text summarization is another important NLP task. Extractive summarization involves selecting a subset of sentences from a text to create a shorter version that retains the most critical information. Abstractive summarization, on the other hand, generates a summary by paraphrasing and rephrasing the original text. The extractive summarization method typically involves the following steps:

1. Sentence Tokenization: Divide the text into individual sentences.

2. Text Preprocessing: Remove stopwords and punctuation, and convert words to lowercase.

3. Calculate Sentence Scores: Assign scores to sentences based on their importance.

4. Select Top Sentences: Choose sentences with the highest scores to form the summary.
"""

# Set the number of sentences you want in the summary (default is 3)
num_sentences_in_summary = 3

result_summary = extractive_summarization(document, num_sentences=num_sentences_in_summary)
print(result_summary)



