# AI-Powered Employee Emotion Analysis and Task Recommendation System

## 📌 Project Overview
This project is an AI-powered system designed to analyze employee emotional states based on textual feedback and recommend suitable tasks accordingly. The goal is to improve employee well-being, productivity, and proactive HR decision-making using data science and machine learning techniques.

The system uses Natural Language Processing (NLP) and a supervised machine learning model to classify emotions such as happiness, stress, boredom, anxiety, and neutrality. Based on the detected emotion, the system recommends appropriate task types and generates analytical insights.


## 🎯 Objectives
- Analyze employee text feedback to detect emotional states
- Recommend suitable tasks based on emotions
- Support HR teams with data-driven insights
- Demonstrate a scalable and ethical AI-based HR analytics prototype


## 🧠 Key Features
- Text preprocessing using NLP techniques
- Emotion classification using Machine Learning
- Rule-based task recommendation system
- Batch prediction and CSV output generation
- Visual analytics for better interpretation
- Modular and scalable project structure


## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Matplotlib
- Seaborn


## 📁 Project Structure
AI_Task_Optimizer/
│
├── data/
│ └── employee_emotions.csv
│
├── src/
│ ├── preprocess.py
│ ├── train_model.py
│ ├── predict_emotion.py
│ ├── task_recommender.py
│ ├── predict_and_recommend.py
│ ├── batch_predict.py
│ └── visualizations.py
│
├── models/
│ ├── emotion_model.pkl
│ └── tfidf.pkl
│
├── outputs/
│ ├── predictions.csv
|
│
├── README.md
└── requirements.txt



## 📊 Dataset Description
The dataset consists of synthetic employee feedback data to ensure privacy and ethical use.  
Each record includes:
- Employee ID
- Text feedback
- Emotion label (happy, neutral, stressed, bored, anxious)


## ⚙️ How the System Works
1. Employee text feedback is collected
2. Text is preprocessed (cleaning, stopword removal)
3. TF-IDF converts text into numerical features
4. A Logistic Regression model predicts emotions
5. A rule-based system recommends suitable tasks
6. Outputs are saved as CSV files
7. Visualizations provide analytical insights


## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries
pip install pandas numpy scikit-learn nltk matplotlib seaborn

2️⃣ Train the Model
python src/train_model.py

3️⃣ Predict Emotion for Sample Input
python src/predict_emotion.py

4️⃣ Predict Emotion and Recommend Task
python src/predict_and_recommend.py

5️⃣ Batch Prediction
python src/batch_predict.py

6️⃣ Generate Visualizations
python src/visualizations.py


📈 Visualizations
The project generates the following graphs:

Employee emotion distribution

Task recommendation distribution

Emotion vs task mapping

These graphs help HR teams understand workforce mood trends and task alignment.


🔒 Data Privacy & Ethics
Uses synthetic data only

No personally identifiable information is stored

Designed to be privacy-safe and ethically compliant


🚀 Future Enhancements
Web application using Flask or FastAPI

Real-time emotion analysis

Integration with HR management systems

Advanced emotion detection using deep learning

Dashboard for HR analytics

👨‍🎓 Project Type
Internship Project / Academic Mini Project
Domain: Data Science, Machine Learning, NLP

✅ Conclusion
This project demonstrates how AI and data science can be applied to improve employee well-being and organizational productivity. It serves as a scalable prototype that can be extended into real-world HR analytics systems.