import random

weather_options = [
    "Холодно",
    "Дощить",
    "Сніжить",
    "Сонячно",
    "Хмарно"
]

def random_weather():
    return random.choice(weather_options)
