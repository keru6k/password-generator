import random
import hashlib

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
length = 1000

def main():
    
    password = []
    for i in range(length):
        password.append(random.choice(chars))
    random.shuffle(password)

    print("the generated password is", "".join(password))
    f = open("generatedpass.txt", "w")
    f.write("".join(password))
    f.close




main()