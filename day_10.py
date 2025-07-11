def encrypt(message,key):
    result=""
    for char in message:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            shifted=(ord(char) -base + key)%26 +base
            result +=chr(shifted)
        else:
            result +=char
    return result

def decrypt(message,key):
    return encrypt(message,-key)



print("secret message program")
choice=input("do you want E or D:").strip().lower()
if choice=="e":
    text=input("enter your message: \n").strip()
    try:
        key=int(input("enter number between 1 and 25: "))
        encrypted=encrypt(text,key)
        print("encrypted message: ")
        print(encrypted)
    except ValueError:
        print("invalid key")
elif choice=='d':
    text=input("enter your encrypted message: \n").strip()
    try:
        key=int(input("enter number between 1 and 25: "))
        decrypted=decrypt(text,key)
        print("decrypted message: ")
        print(decrypted)
    except ValueError:
        print("invalid key")
else:
    print("invalid choice")
