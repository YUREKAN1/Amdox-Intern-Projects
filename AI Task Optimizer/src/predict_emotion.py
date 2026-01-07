import pickle
from preprocess import clean_text

# Load trained model and vectorizer
model = pickle.load(open("models/emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("models/tfidf.pkl", "rb"))

def predict_emotion(text):
    cleaned_text = clean_text(text)
    text_vector = vectorizer.transform([cleaned_text])
    emotion = model.predict(text_vector)[0]
    return emotion

if __name__ == "__main__":
    sample_text = "I am feeling exhausted due to work pressure"
    predicted_emotion = predict_emotion(sample_text)
    print("Predicted Emotion:", predicted_emotion)
