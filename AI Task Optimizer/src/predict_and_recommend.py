import pickle
from preprocess import clean_text
from task_recommender import recommend_task

# Load trained model and vectorizer
model = pickle.load(open("models/emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("models/tfidf.pkl", "rb"))

def predict_emotion_and_task(text):
    cleaned_text = clean_text(text)
    text_vector = vectorizer.transform([cleaned_text])
    emotion = model.predict(text_vector)[0]
    task = recommend_task(emotion)
    return emotion, task

if __name__ == "__main__":
    sample_text = "I am feeling exhausted due to work pressure"
    emotion, task = predict_emotion_and_task(sample_text)

    print("Employee Feedback:", sample_text)
    print("Predicted Emotion:", emotion)
    print("Recommended Task:", task)
