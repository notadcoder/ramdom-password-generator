import random
import string


def generate_password(password_length):
    # Define the character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine the character sets and randomly select characters to create the password
    all_chars = lower + upper + digits + special
    password = ''.join(random.sample(all_chars, password_length))

    return password


# Prompt the user for the length of the password
length = int(input("Enter the length of the password: "))

# Generate 10 passwords and print them to the console
for i in range(10):
    generated_password = generate_password(length)
    print("Password {}: {}".format(i+1, generated_password))
