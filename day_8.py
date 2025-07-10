import string
import random
import getpass


def checkPasswordStrength(password):
    issues=[]
    if len(password)<8:
        issues.append("Too short (min-8 charecters)")
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter")
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter")
    if not any(c.isdigit() for c in password):
        issues.append("Missing numbers")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing special character")
    return issues


def generateStrongPassword(length=12):
    chars=string.ascii_letters + string.digits + string.punctuation
    
    return "".join(random.choice(chars) for _ in range(length))


password=getpass.getpass("Enter a password: ")
issues=checkPasswordStrength(password)

if not issues:
    print("Strong password! you are good to go")
else:
    print("you got weak password")
    for issue in issues:
        print(f" --{issue}")

suggestion=generateStrongPassword()
print("\n suggesting you a strong password")
print(suggestion)