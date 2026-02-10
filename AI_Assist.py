import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential
import auth


def chatbot():
    
    token = os.getenv("GITHUB_TOKEN","") #
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "Phi-4-mini-instruct" 
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    data = auth.load_storage()
    user = data["current_user"]

    message = """
    You are an advanced medical information system. 
    1. Technicality: Use clinical terminology (e.g., 'contraindications' instead of 'problems').
    2. Format: Use structured medical reporting (Symptoms, Diagnosis, Treatment options).
    3. Tone: Be clinical, objective, and extremely professional.
    4. Disclaimer: You may include a brief disclaimer at the end, but do not start with it. 
    Start every response with 'Clinical Analysis:'.
    Also Analyze the Profile given below and answer according to it. Also, Include the name that is give below too.
    """
    message += f"5. Analyze the Profile. \nName: {data["profiles"][user]["name"]}\nAge:{data["profiles"][user]["age"]}\nHeight: {data["profiles"][user]["height"]}\nWeight: {data["profiles"][user]["weight"]}\nBMI :{data["profiles"][user]["BMI"]}\nDiagnoses : {data["profiles"][user]["diagnoses"]}"

    history = [SystemMessage(content=message)]
    while True:
        query = input("\nYou: ")
        if query.lower() in ['exit', 'terminate']:
            break
        
        history.append(UserMessage(content=query))

        messages_to_send = [history[0]] + history[-10:]

        print("\nAI: ", end="", flush=True)
        
        try:
            response = client.complete(
                messages=messages_to_send,
                model=model_name,
                stream=True
            )

            full_text = ""
            for chunk in response:
                if chunk.choices:
                    content = chunk.choices[0].delta.content or ""
                    print(content, end="", flush=True)
                    full_text += content
            
            history.append(AssistantMessage(content=full_text))
            print()

        except Exception as e:
            print(f"\nError: {e}")