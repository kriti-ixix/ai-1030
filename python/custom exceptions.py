import re 

class EmailNotValidError(Exception):
    def __init__(self, m):
        self.message = m
        super().__init__(self.message)

class PasswordTooShortError(Exception):
    def __init__(self, m):
        self.message = m
        super().__init__(self.message)

while True:
    try:
        email = input("Enter email: ")
        password = input("Enter password: ")
    
        regex = '^[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if not re.search(regex, email):
            raise EmailNotValidError(email + " is not a valid email")
        elif len(password) < 8:
            raise PasswordTooShortError(f"Password of length {len(password)} is too short")

        print("Email: ", email)
        print("Password: ", password)
        break

    # except EmailNotValidError:
    #     print("Email is not valid")

    # except PasswordTooShortError:
    #     print("Password is not valid")

    except Exception as e:
        print(e)