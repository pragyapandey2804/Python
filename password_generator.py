import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special    

    while True:
        pwd = ''.join(random.choice(characters) for i in range(min_length))
        
        if numbers and not any(char in digits for char in pwd):
            continue
        if special_characters and not any(char in special for char in pwd):
            continue
        
        return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have a number (y/n)? ").lower() == "y"
has_special = input("Do you want to have a special character (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
