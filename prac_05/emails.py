def main():
    email_users = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirmation = input("Is your name {}? (Y/n)".format(name)).title()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_users[email] = name
        email = input("Email: ")
    for email, name in email_users.items():
        print(name, f"({email})")


def get_name(email):
    name_section = email.split('@')[0]
    name_components = name_section.split('.')
    name = " ".join(name_components).title()
    return name


main()
