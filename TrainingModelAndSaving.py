import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
data = pd.read_csv(r'E:\1.csv')

# Separate features (text) and labels (0 or 1)
X = data['text']
y = data['label']

# Split the data into training and testing sets ===> Don't ask why these numbers...
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer    
vectorizer = TfidfVectorizer(lowercase=True, strip_accents='ascii', stop_words='english') # !! why not utf-8? !!

# Fit and transform the training data with TF-IDF vectorizer
X_train_tfidf = vectorizer.fit_transform(X_train)

# Transform the test data using the same vectorizer
X_test_tfidf = vectorizer.transform(X_test)

# Create a Support Vector Machine (SVM) classifier
classifier = SVC(kernel='linear', C=1.0, probability=True)  # Enable probability estimates

# Train the SVM classifier on the training data
classifier.fit(X_train_tfidf, y_train)

# Save the trained model to a file
joblib.dump(classifier, 'shakespeare_model.joblib')

# Save the TF-IDF vectorizer
joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')

# Make predictions on the test data
y_pred = classifier.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Classification Report:")
print(classification_report(y_test, y_pred))


"""# Train the SVM classifier on the training data
classifier.fit(X_train_tfidf, y_train)

# Save the trained model to a file
joblib.dump(classifier, 'shakespeare_model.joblib')

# Save the TF-IDF vectorizer
joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')
"""
