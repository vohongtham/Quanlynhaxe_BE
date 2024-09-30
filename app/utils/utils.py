# app/utils/utils.py
import random
import string

def generate(length=6):
    """Generate a random user ID with uppercase letters and numbers, starting with 'NX'."""
    characters = string.ascii_uppercase + string.digits  # Use only uppercase letters and digits
    user_id = '' + ''.join(random.choice(characters) for _ in range(length - 0))
    return user_id
