import random
from .responses import motivates


def random_motivation():
    return random.choice(motivates)
