import random

def create_key(keylen):
    return [random.randint(0, 255) for i in range(0, keylen)]
