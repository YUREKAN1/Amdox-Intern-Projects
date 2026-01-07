import pandas as pd
import pickle
from preprocess import clean_text
from task_recommender import recommend_task

# Load model
model = pickle.load(open("models/emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("models/tfidf.pkl", "rb"))

# Load dataset
df = pd.read_csv("data/employee_emotions.csv")

# Clean text
df['clean_text'] = df['text_feedback'].apply(clean_text)

# Predict emotion
X_vec = vectorizer.transform(df['clean_text'])
df['predicted_emotion'] = model.predict(X_vec)

# Recommend task
df['recommended_task'] = df['predicted_emotion'].apply(recommend_task)

# Save output
df[['employee_id', 'text_feedback', 'predicted_emotion', 'recommended_task']] \
    .to_csv("outputs/predictions.csv", index=False)

print("Batch prediction completed. File saved to outputs/predictions.csv")
