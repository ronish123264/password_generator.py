import random
import string

def generate_password(length):
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    character = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password += [random.choice(character)for _ in range(length-4)]
    
    random.shuffle(password)
    
    return "" .join(password)


length = int(input("Enter the length of the password (min 8): "))
if length < 8:
    print("The length of the password must be at least 8 !!")
    exit()
    
password = generate_password(length)
print(f"The generated password is: {password}")



