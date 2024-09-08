# Sentiment Analysis Program with Emotion Mapping and File Handling
# ---------------------------------------------------------------
# This program allows users to input feedback and performs sentiment analysis using the TextBlob library. 
# Based on the sentiment (positive, negative, neutral), it maps the sentiment to an emotion and stores the feedback 
# in a file corresponding to the sentiment. The program also allows users to retrieve and view all feedbacks 
# of a certain sentiment from the respective files.

# Prerequisites:
# 1. Install the 'textblob' library for sentiment analysis:
#    Run: `pip install textblob`
# 2. The program uses the 'nltk' library for natural language processing tasks. Ensure it is installed:
#    Run: `pip install nltk`
# 3. The program will create or append feedback to text files named 'positive.txt', 'negative.txt', and 'neutral.txt'.

from textblob import TextBlob  # Import the TextBlob library for sentiment analysis
import nltk  # Import nltk to handle natural language processing tasks
nltk.download('stopwords')  # Download stopwords 

# This function analyzes the sentiment of the given text and maps it to an emotion
def get_feedback_sentiment(text):
    blob = TextBlob(text)  # Create a TextBlob object to analyze the text
    polarity = blob.sentiment.polarity  # Polarity is a value between -1 (negative) and 1 (positive)
    
    # Determine sentiment based on polarity score
    if polarity > 0:
        return 'positive', map_to_emotion('positive')  # Positive sentiment
    elif polarity < 0:
        return 'negative', map_to_emotion('negative')  # Negative sentiment
    else:
        return 'neutral', map_to_emotion('neutral')  # Neutral sentiment

# This function maps sentiment to an emotional reaction
def map_to_emotion(sentiment):
    # Map sentiment to corresponding emotions using emoji representations
    emotion_map = {
        'positive': 'joyful 😊',        # Positive sentiment leads to a joyful reaction
        'negative': 'disappointed 😔',  # Negative sentiment leads to a disappointed reaction
        'neutral': 'indifferent 😐'     # Neutral sentiment leads to an indifferent reaction
    }
    return emotion_map.get(sentiment, 'neutral')  # Return the emotion for the sentiment

# This method adds a new review to a text file based on the sentiment
def add_review_to_file(review, sentiment):
    file_path = f"{sentiment}.txt"  # File path based on sentiment (positive, negative, neutral)
    with open(file_path, 'a') as file:  # Open the file in append mode
        file.write(f"{review}\n")  # Write the review to the file

# This function reads review data from a file and returns it as a list
def read_data_from_file(file_path):
    data = []  # List to hold reviews
    with open(file_path, 'r') as file:  # Open the file in read mode
        for line in file:
            data.append(line.strip())  # Strip trailing spaces/newlines and add to data list
    return data  # Return the list of reviews

# This function displays all reviews of a specific sentiment along with predicted sentiment and emotion
def showAllReview(sentiment):
    file_path = f"{sentiment}.txt"  # File path based on sentiment
    data = read_data_from_file(file_path)  # Get review data from file
    for review in data:
        predicted_sentiment, emotion = get_feedback_sentiment(review)  # Analyze sentiment
        print(f"Text: {review}")  # Display the review text
        print(f"Expected Sentiment: {sentiment}")  # Display the expected sentiment
        print(f"Predicted Sentiment: {predicted_sentiment}")  # Show the predicted sentiment
        print(f"Emotion: {emotion}")  # Show the mapped emotion
        print(" - " * 50)  # Divider for clarity in output

# Main loop to continuously accept user input for sentiment analysis and display options
while True:
    # Instructions for user input and options
    print("-" * 100)
    user_input = input("Enter feedback for sentiment analysis (or Type: \n Type 'exit' to quit:\n"
                       "Type 'positive' to display all positive reviews:\n"
                       "Type 'negative' to display all negative reviews:\n"
                       "Type 'neutral' to display all neutral reviews:\n"
                       + "-" * 100 + "\nEnter your Input here ->   \n")
    
    # Exit the loop if user types 'exit'
    if user_input.lower() == 'exit':
        break
    # Display all negative reviews if user types 'negative'
    elif user_input.lower() == 'negative':
        showAllReview("negative")
    # Display all positive reviews if user types 'positive'
    elif user_input.lower() == 'positive':
        showAllReview("positive")
    # Display all neutral reviews if user types 'neutral'
    elif user_input.lower() == 'neutral':
        showAllReview("neutral")
    # Analyze the user's input and save it to the appropriate file
    else:
        user_predicted_sentiment, user_emotion = get_feedback_sentiment(user_input)  # Analyze input
        print(f"User Feedback: {user_input}")  # Display user feedback
        print(f"Predicted Sentiment: {user_predicted_sentiment}")  # Show predicted sentiment
        add_review_to_file(user_input, user_predicted_sentiment)  # Add the new review to the file
        print(f"Emotion: {user_emotion}")  # Show corresponding emotion
        print(" - " * 50)  # Divider for clarity
