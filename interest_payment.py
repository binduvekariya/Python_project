def payment():
    print("this is a monthly payment loan calculator: ")
    print("")

    principal = float(input("enter your principal amount: "))
    rate = float(input("enter the annual interst rate: "))
    years = int(input("enter amount of years: "))

    monthly_interest_rate = rate / 1200
    amount_of_month = years * 12
    monthly_payment = (principal * monthly_interest_rate / (1 - (1+monthly_interest_rate) ** (-amount_of_month)))

    print("the monthly payment for this loan is: %.2f" %monthly_payment)

payment()