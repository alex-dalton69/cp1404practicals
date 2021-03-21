# Version 1
"""MIN_LENGTH = 8
password = str(input("Password: "))
while len(password) < MIN_LENGTH:
    print("Error, password must be a minimum of {} characters long.".format(MIN_LENGTH))
    password = str(input("Password: "))
if len(password) >= MIN_LENGTH:
    print("*" * len(password))"""

# Version 2
MIN_LENGTH = 8


def main():
    password = get_password()
    display_asterisks(password)


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Error, password must be a minimum of 8 characters long.")
        password = str(input("Password: "))
    return password


def display_asterisks(password):
    print("*" * len(password))


main()
