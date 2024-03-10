import random
from random import randint


def password_generator(*, letters=True, symbols=False, numbers=False, duplicates=False, pass_length=8):
    """
    letters - приймає True або False, за замовчуванням True (відповідає за наявність літер в паролі верхнього і нижнього регістру)
    symbols - приймає True або False, за замовчуванням False (відповідає за наявність символів(!@#$%^&*()+) в паролі)
    numbers - приймає True або False, за замовчуванням False (відповідає за наявність цифр в паролі)
    duplicates - приймає True або False, за замовчуванням False(відповідає за наявність дублікатів символів)
    pass_length - приймає ціле число, за замовчуванням 8 (довжина паролю)
    """

    letters_data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols_data = "!@#$%^&*()+"
    numbers_data = "0123456789"
    compared_data = letters_data + symbols_data + numbers_data
    resulted_password = ""

    if pass_length < 8:
        return f"Your password is too short, symbols = {len(pass_length)}"

    # generating random letters with length = pass_length
    if letters:
        for i in range(pass_length):
            resulted_password += letters_data[randint(0, len(letters_data) - 1)]

    # generating random symbols with length = pass_length
    if symbols:
        for i in range(pass_length):
            resulted_password += symbols_data[randint(0, len(symbols_data) - 1)]

    # generating random numbers with length = pass_length
    if numbers:
        for i in range(pass_length):
            resulted_password += numbers_data[randint(0, len(numbers_data) - 1)]

    # choose random letters, symbols, numbers with length = pass_length
    resulted_password = random.sample(resulted_password, pass_length)

    # checking current letter and next one, if they are duplicated I choose and replace current symbol to new one
    # from compared_data string
    if duplicates:
        for i in range(len(resulted_password) - 1):
            if resulted_password[i] == resulted_password[i + 1]:
                resulted_password[i] = compared_data[randint(0, len(compared_data) - 1)]

    return ''.join(resulted_password)


print(password_generator(letters=True, symbols=True, numbers=True, duplicates=True, pass_length=8))
# print(password_generator(True, True, True, True, 8)) # will be error because arguments are positional
