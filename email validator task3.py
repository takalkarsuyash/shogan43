import re

pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def email_validator(email):
    if re.fullmatch(pattern,email):
        print("valid email")
    else:
        print("invalid email")


email=input("enter the email")
validator=email_validator(email)
print(validator)



