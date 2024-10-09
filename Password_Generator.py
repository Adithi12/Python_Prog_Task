import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password with the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Prompt the user to specify the desired length of the password
try:
    length = int(input("Enter the desired password length: "))
    
    if length < 4:
        print("Password length should be at least 4 characters for better security.")
    else:
        # Generate and display the password
        generated_password = generate_password(length)
        print(f"Generated Password: {generated_password}")
except ValueError:
    print("Please enter a valid number.")