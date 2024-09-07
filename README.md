This project is a simple sentiment analysis tool that analyzes user feedback or predefined reviews, classifies the sentiment (positive, negative, or neutral), 
and maps it to an emotional reaction (e.g., joyful 😊, disappointed 😔, indifferent 😐).
It uses TextBlob for sentiment analysis and supports both file-based and user input processing.

**Features**
Sentiment Detection: Identifies whether feedback is positive, negative, or neutral.
Emotion Mapping: Converts sentiment to emotions based on the analysis.
File Handling: Reads reviews from a file (sentiment_data.txt).
User Input: Allows users to input their own feedback for analysis.

**Installation**
Clone the repository:
git clone https://github.com/pRoMasteR2002/sentiment-analysis-feedback.git

Install the required libraries:
pip install textblob nltk

Download the stopwords corpus (if needed):
import nltk
nltk.download('stopwords')

**How to Run**
Ensure that the review data is stored in the sentiment_data.txt file, with each line containing a review and expected sentiment, separated by a comma (e.g., I love this movie!,positive).

Run the script:
python sentiment_analysis.py

You can also input your own feedback after the initial file-based analysis.

**Example Input (from sentiment_data.txt)**
I love this movie!,positive
This was a terrible experience,negative
It's an average performance,neutral
