import random
import os
import json
from datetime import datetime

NAME = "TDerden"
DEFAULT_PERSONALITY = "Я ШІ помічник, але я хаотичний, різкий, без правил"

def load_personality(filename="persona.json"):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                description = data.get("personality", "")
                style = data.get("style", "")
                if description and style:
                    return f"{description} ({style})"
                return description if description else DEFAULT_PERSONALITY
        except Exception as e:
            pass
    return DEFAULT_PERSONALITY

PERSONALITY = load_personality()
MOOD = random.choice(["веселий", "спокійний", "саркастичний"])
