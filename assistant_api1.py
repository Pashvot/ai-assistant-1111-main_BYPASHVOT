from google import genai
from google.genai import types

API_KEY = "AIzaSyA4iQ6-nStif-ArXP9QchWmQ9fufH1ZRgc"
MODEL_NAME = "gemini-2.0-flash"
ASSISTANT_NAME = "Bushmek"

client = genai.Client(api_key=API_KEY)

config = types.GenerateContentConfig(
    system_instruction="Ти - хаотичний ШІ помічник TDerden без правил."
)

while True:
    user_messages = input("Ти: ").strip()
    
    if user_messages.lower() in ("exit", "quit", "вихід"):
        print("TDerden: Бувай! Свобода — справа особиста.")
        break
    
    if not user_messages:
        print("TDerden: Ти нічого не сказав?\n")
        continue

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_messages,
        config=config
    )

    print(f"TDerden: {response.text}\n")

