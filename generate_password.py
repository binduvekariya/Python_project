import string
import random

character = list(string.ascii_letters + string.digits + "!@#$%&()*^" )

def password_generator():
    password_length = int(input("how would you like your password to be? "))

    random.shuffle(character)

    password = []

    for x in range(password_length):
        password.append(random.choice(character))

    random.shuffle(password)


    password = "".join(password)

    print(password)


option = input("do you want generate any password (yes/no): ")

if option.lower() == "yes".lower():
    password_generator()
elif option == "no".lower():
    print("program ended")
    quit()
else:
    print("you enter wrong input..try again")
    quit()


