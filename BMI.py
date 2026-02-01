import csv
import datetime
import os
import manager
import auth

def log_bmi(username, bmi_val, output_path='bmi_logs.csv'):
    file_needs_header = not os.path.exists(output_path) or os.path.getsize(output_path) == 0
    with open(output_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if file_needs_header:
            writer.writerow(['User', 'BMI', 'Computed on'])
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([username, bmi_val, timestamp])

    manager.update_profile('BMI', bmi_val)

def calculate(height, weight):
    data = auth.load_storage()
    try:
        h = float(height)
        w = float(weight)

        if h > 3:
            h = h / 100.0
            
        bmi_val = round(w / (h ** 2), 2)
        
        log_bmi(data["current_user"], bmi_val)
        return bmi_val
    except (ZeroDivisionError, ValueError):
        print("Error: Invalid height or weight values.")
        return 0

def get_bmi_history(username, path='bmi_logs.csv'):
    history = []
    if not os.path.exists(path):
        return history
    
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['User'] == username:
                history.append(row)
    return history
