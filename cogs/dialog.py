from datetime import datetime
from .jokes import random_joke
from .motivations import random_motivation
from .personal import random_personal
from .facts import random_fact
from .empty_responses import random_empty
from .weather import random_weather
from .fallback import random_fallback
from .notes import add_note, read_notes, clear_notes
from .profile import add_fact, show_profile
from .constants import NAME


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
    elif "запиши в нотатки" in t or "додай в нотатки" in t:
        return "add note"
    elif "покажи нотатки" in t or "прочитай нотатки" in t:
        return "read notes"
    elif "профіль" in t:
        return "profile"
    elif "додай факт про мене" in t:
        return "add fact"
    elif "видали нотатки" in t:
        return "clear notes"
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
        return "На данний момент я можу реагувати на команди: 'жарт', 'мотивація', 'хто ти', 'час', 'погода', 'факт', 'запиши в нотатки', 'покажи нотатки', 'профіль', 'додай факт про мене'"
    elif tag == "weather":
        return f"За прогнозом - {random_weather()}"
    elif tag == "add note":
        print(f"{NAME}: Що саме мені записати?")
        while True:
            user_input = input("Ти: ").strip()
            if user_input:
                return add_note(user_input)
            else:
                print(f"{NAME}: Та ну! Напиши щось, щоб я міг це записати.")
    elif tag == "read notes":
        return read_notes()
    elif tag == "clear notes":
        return clear_notes()
    elif tag == "add fact":
        print(f"{NAME}: Який факт мені записати про тебе?")
        fact = input("Ти: ").strip()
        return add_fact(fact)
    elif tag == "profile":
        return show_profile()
    else:
        return random_fallback()
