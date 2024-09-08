
---

# Sentiment Analysis Tool

This project is a sentiment analysis tool that classifies user feedback or predefined reviews as positive, negative, or neutral. It maps each sentiment to an emotional reaction (e.g., joyful 😊, disappointed 😔, indifferent 😐). The tool uses TextBlob for sentiment analysis and supports both file-based and user input processing.

## Features

- **Sentiment Detection:** Identifies feedback sentiment as positive, negative, or neutral.
- **Emotion Mapping:** Converts sentiment to corresponding emotions using emojis.
- **File Handling:** Stores feedback in separate text files (`positive.txt`, `negative.txt`, `neutral.txt`) based on sentiment.
- **User Input:** Allows users to input their own feedback for real-time sentiment analysis.
- **Review Retrieval:** Enables viewing of all stored feedback for a specific sentiment.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pRoMasteR2002/HexSoftwares_Project_Sentiment-Analysis.git
   ```

2. **Install the required libraries:**

   ```bash
   pip install textblob nltk
   ```

3. **Download the stopwords corpus (if needed):**

   ```python
   import nltk
   nltk.download('stopwords')
   ```

## How to Run

1. **Ensure the required files are present:**
   - The program will create or append to `positive.txt`, `negative.txt`, and `neutral.txt` based on user input.

2. **Run the script:**

   ```bash
   python sentiment_analysis.py
   ```

3. **Interaction:**
   - You can enter feedback for sentiment analysis directly.
   - Type 'exit' to quit.
   - Type 'positive', 'negative', or 'neutral' to display all reviews of that sentiment.

## Example

**User Input:**
- Type a feedback: "I love this movie!"
- Type 'positive', 'negative', or 'neutral' to view relevant reviews.

**Example Reviews in `sentiment_data.txt` (for legacy use):**
```
I love this movie!,positive
This was a terrible experience,negative
It's an average performance,neutral
```

---
