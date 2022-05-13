from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def get_sentiment(query_sentence):
    """
    """
    sentiment = sentiment_model(query_sentence)
    return sentiment
