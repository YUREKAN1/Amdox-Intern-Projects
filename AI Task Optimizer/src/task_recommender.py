def recommend_task(emotion):
    if emotion == "happy":
        return "Assign creative or challenging tasks"
    elif emotion == "neutral":
        return "Assign routine or maintenance tasks"
    elif emotion == "bored":
        return "Assign learning or skill development tasks"
    elif emotion == "stressed":
        return "Assign light workload or flexible tasks"
    elif emotion == "anxious":
        return "Assign collaborative or supportive tasks"
    else:
        return "No suitable task recommendation available"
