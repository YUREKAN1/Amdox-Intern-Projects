import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from preprocess import clean_text
from sklearn.metrics import classification_report, confusion_matrix

# After training
y_pred = model.predict(X_vec)

print("Classification Report:\n")
print(classification_report(y, y_pred))

print("Confusion Matrix:\n")
print(confusion_matrix(y, y_pred))


# Load dataset
df = pd.read_csv("data/employee_emotions.csv")

# Preprocess text
df['clean_text'] = df['text_feedback'].apply(clean_text)

# Features and labels
X = df['clean_text']
y = df['emotion']

# Convert text to numerical features
vectorizer = TfidfVectorizer(max_features=300)
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# Save model and vectorizer
pickle.dump(model, open("models/emotion_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/tfidf.pkl", "wb"))

print("Model training completed successfully.")
