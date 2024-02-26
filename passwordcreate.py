"""Generate a random password of a specified length.

Input values: Set length not to exceed 20 

Output value:

Randomly generated passwords of the specified length.

"""

import random
import string


def generate_password(length=20):
    alphabet = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    # Ensure length doesn't exceed 20 chars
    length = int(input("Enter password length: "))

    # Combine char sets for random.sample to pull from
    characters = alphabet + numbers + symbols

    # Generate password
    password = "".join(random.sample(characters, length))
    return password

    # Driver code example


generated_password = generate_password()
print(
    "New password: ", generated_password
)  # Prints New password:  I[@Q-N)MW}rU<7vp&PO5


def generate_password2(length=20):

    num_amount = 9
    sample_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%^&*"

    password = []

    for i in range(11):
        ran_num = random.randint(0, num_amount)
        password.append(ran_num)
    print(password)
    for i in range(int(length // 2)):
        ran_letter = random.sample(sample_string, 9)
    password.extend(ran_letter)
    print(password)
    return password


pw = generate_password2()
print(
    "The newly generated password is: ", pw
)  # prints The newly generated password is:  [8, 8, 6, 5, 6, 8, 4, 3, 6, 2, 7, 'r', 'a', '^', 'j', 'l', 'F', 'K', 'H', 'B']
