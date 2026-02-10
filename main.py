import auth
import BMI
import manager
import AI_Assist

def show_history(username):
    records = BMI.get_bmi_history(username)
    print(f"\n--- BMI HISTORY FOR {username} ---")
    if not records:
        print("No previous records found.")
    else:
        print(f"{'Date':<20} | {'BMI Score':<10}")
        print("-" * 35)
        for r in records:
            print(f"{r['Computed on']:<20} | {r['BMI']:<10}")
    print("-" * 35)

def main():
    user_session = None

    while True:
        if not user_session:
            print("\n[1] Login / Register\n[2] Exit")
            choice = input("Select: ")
            if choice == "1":
                user_session = auth.login_user()
            elif choice == "2": 
                break
        else:
            u = user_session['current_user']
            
            data = auth.load_storage()
            profile = data["profiles"].get(u, {})

            print(f"\n--- HEALTH DASHBOARD: {u} ---")
            print("1. View Profile & Active Diagnoses")
            print("2. Update Profile (Weight/Name/Pass/Calories)")
            print("3. Add New Diagnosis")
            print("4. Calculate & Log Current BMI")
            print("5. View BMI Progress History")
            print("6. Chat with AI")
            print("7. Logout")
            print("8. Exit")
            
            choice = input("Select: ")

            if choice == "1":
                print(f"\n[PROFILE] Name: {profile.get('name', u)}")
                print(f"[VITALS] Weight: {profile.get('weight')}kg | BP: {profile.get('BP')}")
                import datetime
                today = datetime.datetime.now().strftime('%Y-%m-%d')
                daily_cal = profile.get('calories', {}).get(today, 0)
                print(f"[CALORIES TODAY] {daily_cal} kcal")
                print(f"[MEDICAL HISTORY] {', '.join(profile.get('diagnoses', ['None']))}")
            
            elif choice == "2":
                print("\nUpdate: 1. Weight  2. Password  3. Name  4. Calories")
                sub = input("Select: ")
                if sub == "1":
                    manager.update_profile("weight", int(input("New weight (kg): ")))
                elif sub == "2":
                    manager.update_profile("password", input("New password: "))
                elif sub == "3":
                    manager.update_profile("name", input("New name: "))
                elif sub == "4":
                    manager.add_calories(int(input("Amount of Calories (kcal): ")))
            
            elif choice == "3":
                disease = input("Enter diagnosis: ")
                manager.add_diagnosis(disease)

            elif choice == "4":
                bmi = BMI.calculate(profile['height'], profile['weight'])
                print(f"Current BMI logged: {bmi}")

            elif choice == "5":
                show_history(u)

            elif choice == "6":
                print("This AI is Phi-4 Mini, provided by Microsoft. It can make mistakes, be careful with the responses.")
                AI_Assist.chatbot()

            elif choice == "7":
                data = auth.load_storage()
                data["status"] = "inactive"
                auth.save_storage(data)
                user_session = None
                print("Logged out successfully.")

            elif choice == "8":
                print("Exiting... Stay healthy!")
                break

if __name__ == "__main__":
    main()
