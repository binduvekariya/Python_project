def add(a,b):
    answer = a+b
    print(str(a) +" + " + str(b) +" = " + str(answer) + "\n")

def sub(a,b):
    answer = a-b
    print(str(a) + "+" + str(b) + " = " + str(answer) + "\n")

def mul(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + " = " + str(answer) + "\n")

def div(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + " = " + str(answer) + "\n")

while(True):  
    print("A. addition")
    print("B. subtraction")
    print("C. multiplication")
    print("D. division")
    print("E. exit")
    choice = input("Enter your choice: ")

    if choice=="A" or choice=="a":
        print("addition")
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        add(a,b)
    
    elif choice=="B" or choice=="b":
        print("subtraction")
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        sub(a,b)

    elif choice=="c" or choice=="C":
        print("multipliction")
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        mul(a,b)

    elif choice=="D" or choice=="d":
        print("division")
        a = int(input("enter 1st number: "))
        b = int(input("enter 2nd number: "))
        div(a,b)

    elif choice=="E" or choice=="e":
        print("program end")
        quit()