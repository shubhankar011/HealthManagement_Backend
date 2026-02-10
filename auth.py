import json
import hashlib
import os
import requests

DB_FILE = "users_data.json"
CLOUD_URL = "https://api.jsonstorage.net/v1/json/222ef668-b846-41a2-8410-c177f9555acd/66a19b59-4c91-4e38-8a62-add9e290073d?apiKey=7d462981-38e2-4265-8635-c2e74c41c457"

def hash_pw(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_storage():
    if not os.path.exists(DB_FILE):
        return {"users": {}, "profiles": {}, "status": "inactive", "current_user": None}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_storage(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
    try:
        headers = {'Content-Type': 'application/json'}
        requests.put(CLOUD_URL, data=json.dumps(data), headers=headers)
        print("Cloud synced successfully!")
    except Exception as e:
        print(f"Cloud Sync Error: {e}")

def login_user():
    data = load_storage()
    if not data["users"]:
        print("--- First Time Setup ---")
        u = input("Create Username: ")
        p = input("Create Password: ")
        data["users"][u] = hash_pw(p)
        data["profiles"][u] = {
            "name": input("Enter your name: "),
            "age": int(input("Enter Age: ")),
            "height": int(input("Enter Height (cm): ")),
            "weight": int(input("Enter Weight (kg): ")),
            "BP": input("Enter Blood Pressure: "),
            "calories": {},
            "diagnoses": []
        }
        data["current_user"] = u
        data["status"] = "active"
        save_storage(data)
        return data
    
    if data["status"] == "active" and data.get("current_user"):
        return data
    
    print("--- Login ---")
    u_input = input("Username: ")
    p_input = input("Password: ")

    if u_input in data["users"] and data["users"][u_input] == hash_pw(p_input):
        data["status"] = "active"
        data["current_user"] = u_input
        save_storage(data)
        return data
    return None
