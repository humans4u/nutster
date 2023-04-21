import string
import random

def server_name(n=10):
    char = string.ascii_lowercase + string.digits
    return "".join(random.choice(char) for i in range(n))