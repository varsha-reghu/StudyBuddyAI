def generate_schedule(subjects):
    schedule = []
    for subject in subjects:
        confidence = subject['confidence']
        base_hours = {
            'low': 4,
            'medium': 2,
            'high': 1
        }.get(confidence, 2)

        total_days = subject['exam_days_left']
        daily_hours = round(base_hours * 1.0, 1)
        schedule.append({
            'day': subject['day'],
            'subject': subject['name'],
            'hours': daily_hours
        })

    return schedule
