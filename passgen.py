import random

def main():
    k = input("For? ") #generatedpass [something].txt
    lengthpass = int(input("Length? ")) #length of the password
    password = []

    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    length = lengthpass

    for i in range(length):
        password.append(random.choice(chars))
    random.shuffle(password)

    print("the generated password is", "".join(password))
    f = open("generatedpass " + k + ".txt", "w")
    f.write("".join(password))
    f.close

main()
