import random
import os
from datetime import datetime

NAME = "TDerden"
DEFAULT_PERSONALITY = "Я ШІ помічник, але я хаотичний, різкий, без правил"

def load_personality(filename="persona.txt"):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    return text
        except Exception as e:
            pass
    return DEFAULT_PERSONALITY

PERSONALITY = load_personality()
MOOD = random.choice(["веселий", "спокійний", "саркастичний"])
