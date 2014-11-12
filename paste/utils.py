
import string
import random

def short_hash():
    return ''.join(random.choice(string.ascii_letters)
                   for _ in range(8))
