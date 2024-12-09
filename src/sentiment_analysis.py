from textblob import TextBlob

class SentimentAnalyzer:
    """
    A simple class for analyzing the sentiment of a text.
    """

    @staticmethod
    def analyze_sentiment(text):
        """
        Analyze the sentiment of the given text.

        Parameters:
        text (str): The text to analyze.

        Returns:
        dict: A dictionary containing polarity and subjectivity scores.
        """
        analysis = TextBlob(text)
        return {
            "polarity": analysis.polarity,  # Ranges from -1 (negative) to 1 (positive)
            "subjectivity": analysis.subjectivity  # Ranges from 0 (objective) to 1 (subjective)
        }
