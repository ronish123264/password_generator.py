import random
import string

def generate_password(length):
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    character = string.ascii_uppercase + string.ascii_lowercase + string.gigits + string.punctuation
    for _ in range(length-4):
        password.append[random.choice(character)]
    
    random.shuffle(password)
    

