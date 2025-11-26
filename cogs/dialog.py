from .jokes import random_joke
from .motivations import random_motivation
from .personal import random_personal
from .facts import random_fact


def get_response(text):
    t = text.lower()

    if "жарт" in t or "насміши" in t:
        return random_joke()

    elif "мотив" in t or "підтримай" in t:
        return random_motivation()

    elif "хто ти" in t or "про себе" in t:
        return random_personal()

    elif "факт" in t or "цікаво" in t:
        return random_fact()

    else:
        return f"Шо? нифига не понял: '{text}'. Мб, норм що то напишеш?"
