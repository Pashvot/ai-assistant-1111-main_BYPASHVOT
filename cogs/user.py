import os
import json
from token import NAME

def load_user():
    if os.path.exists("user.json"):
        try:
            with open("user.json", "r", encoding="utf-8") as file:
                user = file.read().strip()
                if not user:
                    return None
                data = json.loads(user)
                return data.get ("name")
        except Exception:
            return None
    return None

def get_user_name():
    name = load_user()
    if name:
        return name
    
    while True:
        print(f"{NAME}: Як тебе звати?")
        ask_name = input("Ти: ").strip()
        if not ask_name:
            print(f"{NAME}: Приємно познайомитись, {ask_name}!")
        else:
            with open("user.json", "w", encoding="utf-8") as file:
                json.dump({"name": ask_name}, f)
            return ask_name