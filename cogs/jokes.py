import random
from .responses import jokes


def random_joke():
    return random.choice(jokes)
