# Password Generator in Python
# Author: Keru6k

# Changes: Added choices to remove "L" and "I" to the generated password
# Reason: I almost fucked up my exam time because i can't distinguish the L and I on the password i've generated. (I had to manually type it out)
# its a dumb reason but hey, someone (or me) might need this in the future lul

import random
import os
import time

def main():

    k = input("For? ") #generatedpass [something].txt
    lengthpass = int(input("Length? "))
            
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    charsNoLi = "0123456789abcdefghjkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    length = lengthpass
    agree = "yes"
    disagree = "no"

    def choose():
        choiceForRemv = str(input("remove L and i to be less confusing? [YES]  [NO] "))
        if (choiceForRemv == agree) or (choiceForRemv.lower() == agree.lower()) or choiceForRemv.upper == agree.upper():
            password = []
            for i in range(length):
                password.append(random.choice(charsNoLi))
            random.shuffle(password)

            print("the generated password is", "".join(password))
            f = open("generatedpass " + k + ".txt", "w")
            f.write("".join(password))
            f.close
            input("Press any to exit ")
            exit()
        elif (choiceForRemv == disagree) or (choiceForRemv.lower() == disagree.lower()) or choiceForRemv.upper == disagree.upper():
            # args above means that even with different capitalizations like "nO", "NO", and "No" are still considered valid answers
            password = []
            for i in range(length):
                password.append(random.choice(chars))
            random.shuffle(password)

            print("the generated password is", "".join(password))
            f = open("generatedpass " + k + ".txt", "w")
            f.write("".join(password))
            f.close
            input("Press any to exit ")
            exit()
        else:
            print("Please choose a valid answer.")
            time.sleep(2)
            os.system("cls")
            choose()
    choose()

main()
