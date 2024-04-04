def is_leap_year(year):
    
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print("The year is leap year ")
            else: 
                print("The year is not leap year ")
        else:
            print("The year is leap year ")

    else:
        print("This year not a leap year ")

year = int(input("Enter any year you want to check leap year or not: "))
is_leap_year(year)



