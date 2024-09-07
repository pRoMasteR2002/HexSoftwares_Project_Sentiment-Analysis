# Required Libraries and How to Run the Code:
# 1. Install the required libraries by running the following commands in your terminal:
#    pip install textblob nltk
# 2. Save this script as 'sentiment_analysis.py' in your project folder.
# 3. Create a text file 'sentiment_data.txt' in the same folder with reviews and their expected sentiments.
# 4. Run the script in the terminal using:
#    python sentiment_analysis.py

from textblob import TextBlob  # Import TextBlob for sentiment analysis
import nltk  # Import nltk for natural language processing tasks
nltk.download('stopwords')  # Download common words like 'the', 'is', etc. 

# SECTION 1: Function to Analyze Feedback Sentiment
# This function takes a piece of text (feedback or review) and returns its sentiment (positive, negative, or neutral)
# and an associated emotion based on the sentiment.
def get_feedback_sentiment(text):
    blob = TextBlob(text)  # Create a TextBlob object to analyze the text
    polarity = blob.sentiment.polarity  # Get the polarity score (-1 to 1, where -1 is negative and 1 is positive)
    
    # Determine sentiment based on polarity score
    if polarity > 0:
        return 'positive', map_to_emotion('positive')  # Positive sentiment and emotion
    elif polarity < 0:
        return 'negative', map_to_emotion('negative')  # Negative sentiment and emotion
    else:
        return 'neutral', map_to_emotion('neutral')  # Neutral sentiment and emotion

# SECTION 2: Mapping Sentiment to Emotion
# This function takes the sentiment (positive, negative, or neutral) and returns a corresponding emotion.
def map_to_emotion(sentiment):
    # A dictionary that maps each sentiment to an emoji-based emotion
    emotion_map = {
        'positive': 'joyful 😊',        # Joyful for positive sentiment
        'negative': 'disappointed 😔',  # Disappointed for negative sentiment
        'neutral': 'indifferent 😐'     # Indifferent for neutral sentiment
    }
    return emotion_map.get(sentiment, 'neutral')  # Return the mapped emotion or neutral by default

# SECTION 3: Reading Data from File
# This function reads review data from a text file. Each line in the file has a review and its expected sentiment, separated by a comma.
def read_data_from_file(file_path):
    data = []  # List to store reviews and expected sentiments
    with open(file_path, 'r') as file:  # Open the file in read mode
        for line in file:
            parts = line.strip().split(',', 1)  # Split each line by the comma into review and sentiment
            if len(parts) == 2:
                review, sentiment = parts  # Store the review and expected sentiment
                data.append((review, sentiment))  # Add them to the data list
    return data  # Return the list of reviews and expected sentiments

# SECTION 4: Process Reviews from File
# Read and process review data from the text file 'sentiment_data.txt'
file_path = 'sentiment_data.txt'
data = read_data_from_file(file_path)  # Call the function to read data from the file

# Loop through each review and analyze its sentiment
for review, expected_sentiment in data:
    predicted_sentiment, emotion = get_feedback_sentiment(review)  # Analyze the sentiment of the review
    print(f"Text: {review}")  # Display the review text
    print(f"Expected Sentiment: {expected_sentiment}")  # Display the expected sentiment
    print(f"Predicted Sentiment: {predicted_sentiment}")  # Show the predicted sentiment
    print(f"Emotion: {emotion}")  # Show the emotion associated with the sentiment
    print(" - " * 50)  # Divider for clarity in output

# SECTION 5: User Feedback Input
# Allow users to input their own feedback for sentiment analysis
while True:
    user_input = input("Enter feedback for sentiment analysis (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':  # If the user types 'exit', break the loop and end the program
        break
    user_predicted_sentiment, user_emotion = get_feedback_sentiment(user_input)  # Analyze user input
    print(f"User Feedback: {user_input}")  # Display the user's feedback
    print(f"Predicted Sentiment: {user_predicted_sentiment}")  # Display the predicted sentiment for the user's input
    print(f"Emotion: {user_emotion}")  # Display the corresponding emotion for the user's feedback
    print(" - " * 50)  # Divider for clarity in output
