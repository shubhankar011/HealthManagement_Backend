import auth
import datetime
import BMI

def update_profile(field, new_value):
    data = auth.load_storage()
    user = data["current_user"]
    
    if field == "password":
        data["users"][user] = auth.hash_pw(new_value)
    elif field == "name":
        data["profiles"][user]["name"] = new_value
    elif field == "weight":
        data["profiles"][user]["weight"] = new_value
        BMI.calculate(data["profiles"][user]["height"],data["profiles"][user]["weight"])
    else:
        data["profiles"][user][field] = new_value
        
    auth.save_storage(data)
    print(f"Successfully updated {field}!")

def add_calories(amount):
    data = auth.load_storage()
    user = data["current_user"]
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    
    profile = data["profiles"][user]
    if "calories" not in profile:
        profile["calories"] = {}
    
    profile["calories"][today] = profile["calories"].get(today, 0) + int(amount)
    auth.save_storage(data)
    print(f"Added {amount} kcal for {user}.")
def add_diagnosis(disease_name):
    data = auth.load_storage()
    user = data["current_user"]
    profile = data["profiles"][user]
    if "diagnoses" not in profile:
        profile["diagnoses"] = []
    if disease_name not in profile["diagnoses"]:
        profile["diagnoses"].append(disease_name)
        auth.save_storage(data) 
        print(f"Added {disease_name} to your medical history.")
        return True
    else:
        print("This diagnosis is already on record.")
        return False
