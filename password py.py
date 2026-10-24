import random
import string


def make_password(length, use_symbols):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += "!@#$%&*?"

    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password


while True:
    try:
        length = int(input("Password length (8-30): "))
    except ValueError:
        print("Please type a number.")
        continue

    if length < 8 or length > 30:
        print("Choose a length between 8 and 30.")
        continue

    symbols = input("Include symbols? (yes/no): ").lower().strip() == "yes"

    print("Your password:", make_password(length, symbols))

    again = input("Make another? (yes/no): ").lower().strip()
    if again != "yes":
        print("Done!")
        break
