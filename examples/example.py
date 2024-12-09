from src.sentiment_analysis import SentimentAnalyzer

if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    analyzer = SentimentAnalyzer()
    result = analyzer.analyze_sentiment(text)
    print("Sentiment Analysis Result:")
    print(f"Polarity: {result['polarity']}")
    print(f"Subjectivity: {result['subjectivity']}")
