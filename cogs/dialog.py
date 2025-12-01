from datetime import datetime
from .jokes import random_joke
from .motivations import random_motivation
from .personal import random_personal
from .facts import random_fact
from .empty_responses import random_empty
from .weather import random_weather
from .fallback import random_fallback


def analyze(text):
    t = text.lower()
    
    if not text.strip():
        return "empty"
    elif "жарт" in t or "насміши" in t:
        return "joke"
    elif "мотив" in t or "порада" in t or "підтримай" in t:
        return "motivate"
    elif "час" in t or "скільки" in t:
        return "time"
    elif "допомога" in t or "help" in t:
        return "help"
    elif "хто ти" in t or "що ти" in t or "про себе" in t:
        return "personal"
    elif "факт" in t or "цікаво" in t:
        return "fact"
    elif "погода" in t:
        return "weather"
    return "unknown"


def get_response(text):
    t = text.lower()
    tag = analyze(t)
    
    if tag == "empty":
        return random_empty()
    elif tag == "joke":
        return random_joke()
    elif tag == "motivate":
        return random_motivation()
    elif tag == "personal":
        return random_personal()
    elif tag == "fact":
        return random_fact()
    elif tag == "time":
        return f"Зараз {datetime.now().strftime('%H:%M')}"
    elif tag == "help":
        return "На данний момент я можу реагувати на команди: 'жарт', 'мотивація', 'хто ти', 'час', 'погода', 'факт'"
    elif tag == "weather":
        return f"За прогнозом - {random_weather()}"
    else:
        return random_fallback()
