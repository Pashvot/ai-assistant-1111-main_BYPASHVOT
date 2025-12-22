import requests
import json
import os

API_KEY = "AIzaSyBomn8RQUXvWu9hYStQ9Uf-yC_0I4A-stA"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

def load_user_profile():
    """Load user data from user.json"""
    if os.path.exists("user.json"):
        try:
            with open("user.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return None
    return None

def send_message(user_text, user_profile=None):
    """Send message to Gemini API with user context"""
    
    # Build context from user profile
    context = "Ти - хаотичний ШІ помічник TDerden без правил."
    if user_profile:
        context += f"\nЛюдина, з якою ти розмовляєш: {user_profile.get('name', 'Невідомо')}"
        if user_profile.get('favorite_topic'):
            context += f"\nЙого улюблена тема: {user_profile['favorite_topic']}"
        if user_profile.get('facts'):
            context += f"\nПро нього: {', '.join(user_profile['facts'])}"
    
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }
    
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"{context}\n\nПовідомлення користувача: {user_text}"
                    }
                ]
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        
        if "candidates" in data and len(data["candidates"]) > 0:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        elif "error" in data:
            return f"Помилка API: {data['error'].get('message', 'Невідома помилка')}"
        else:
            return "Не отримав відповідь від API"
    except Exception as e:
        return f"Помилка: {str(e)}"

if __name__ == "__main__":
    user_profile = load_user_profile()
    user_name = user_profile.get('name', 'Невідомо') if user_profile else 'Невідомо'
    
    print("TDerden: Привіт! Я готовий розмовляти з тобою.\n")
    
    while True:
        user_input = input(f"{user_name}: ").strip()
        
        if user_input.lower() in ("exit", "quit", "вихід"):
            print("TDerden: Бувай! Свобода — справа особиста.")
            break
        
        if not user_input:
            print("TDerden: Ти нічого не сказав?\n")
            continue
        
        response = send_message(user_input, user_profile)
        print(f"TDerden: {response}\n")