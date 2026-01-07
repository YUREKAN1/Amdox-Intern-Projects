import pandas as pd

def detect_stress(df, threshold=3):
    alerts = []

    for emp_id in df['employee_id'].unique():
        emp_data = df[df['employee_id'] == emp_id]

        stress_count = 0
        for emotion in emp_data['predicted_emotion']:
            if emotion in ['stressed', 'anxious']:
                stress_count += 1
                if stress_count >= threshold:
                    alerts.append({
                        'employee_id': emp_id,
                        'alert': 'Prolonged stress detected'
                    })
                    break
            else:
                stress_count = 0

    return pd.DataFrame(alerts)


if __name__ == "__main__":
    df = pd.read_csv("outputs/predictions.csv")
    alerts_df = detect_stress(df)
    alerts_df.to_csv("outputs/stress_alerts.csv", index=False)
    print(alerts_df)
