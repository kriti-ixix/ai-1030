while True:
    try:
        email = input("Enter email: ")
        password = input("Enter password: ")
        domains = ['com', 'edu', 'co.in', 'org']

        # abc@gmail.com abc123@hotmail.co.in
        # ['abc@gmail', 'com'] ['abc123@hotmail', 'co.in']

        if "@" not in email or email.split('.', 1)[1] not in domains:
            raise IndexError
        elif len(password) < 8:
            raise ArithmeticError

        print("Email: ", email)
        print("Password: ", password)

        break

    except IndexError:
        print("Email is not valid")

    except ArithmeticError:
        print("Password is not valid")