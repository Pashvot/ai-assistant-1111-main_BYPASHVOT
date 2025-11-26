import random
from .responses import greetings


def random_greeting():
    return random.choice(greetings)
