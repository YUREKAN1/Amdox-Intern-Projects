import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load prediction results
df = pd.read_csv("outputs/predictions.csv")

# Set style
sns.set(style="whitegrid")

# -----------------------------
# 1. Emotion Distribution
# -----------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x='predicted_emotion', data=df)
plt.title("Employee Emotion Distribution")
plt.xlabel("Emotion")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -----------------------------
# 2. Task Recommendation Distribution
# -----------------------------
plt.figure(figsize=(10, 5))
sns.countplot(y='recommended_task', data=df)
plt.title("Task Recommendation Distribution")
plt.xlabel("Count")
plt.ylabel("Recommended Task")
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Emotion vs Task Mapping
# -----------------------------
plt.figure(figsize=(10, 6))
sns.countplot(
    x='predicted_emotion',
    hue='recommended_task',
    data=df
)
plt.title("Emotion vs Task Recommendation Mapping")
plt.xlabel("Emotion")
plt.ylabel("Count")
plt.legend(title="Task")
plt.tight_layout()
plt.show()
