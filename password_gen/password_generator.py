import random
import string

# edit for git change
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters 
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False

    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd = pwd + new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd


    # print(letters, digits, special)
min_length = int(input("Enter the minimum length for the password: "))
req_num = input("Number required?(y/n): ").lower() == 'y'
req_special = input("Special character?(y/n): ").lower() == 'y'
pwd = generate_password(min_length,req_num, req_special)
print("The generated password is: ", pwd)