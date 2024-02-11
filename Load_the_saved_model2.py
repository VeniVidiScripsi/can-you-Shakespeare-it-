import joblib
from sklearn.feature_extraction.text import TfidfVectorizer


def load_model_and_vectorizer():
    # Load the saved model
    loaded_model = joblib.load('shakespeare_model.joblib')

    # Load the TF-IDF vectorizer
    vectorizer = joblib.load('tfidf_vectorizer.joblib')

    return loaded_model, vectorizer


def classify_input_text(input_text, model, vectorizer):
    # Transform the input text using the loaded vectorizer
    input_text_tfidf = vectorizer.transform([input_text])

    # Make predictions on the input text
    predictions = model.predict(input_text_tfidf)

    # Get decision function scores for the input text
    decision_scores = model.decision_function(input_text_tfidf)

    # Print the input text, predictions, and decision function scores
    print("Text:", input_text)
    print("Predictions for input text:", predictions)
    print("Decision function scores:", decision_scores)
    print("\n" + "="*50 + "\n")  # Separator for better readability


# Main interactive loop
if __name__ == "__main__":
    # Load the model and vectorizer
    model, vectorizer = load_model_and_vectorizer()

    while True:
        user_input = input("Enter a sentence (or 'exit' to quit): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break

        # Classify the input text
        classify_input_text(user_input, model, vectorizer)
