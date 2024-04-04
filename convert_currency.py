def main():
    print("This program converts  US dollar to Indian rupee")
    print()

    dollar = eval(input("Enter amount of dollar: "))

    rupee = convert_to_rupee(dollar)

    print("that is ",rupee," ruppes")

convert_to_rupee = lambda dollar : dollar*81.28

main()