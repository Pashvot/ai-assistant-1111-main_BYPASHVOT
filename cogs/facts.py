import random
from .responses import facts


def random_fact():
    return random.choice(facts)
