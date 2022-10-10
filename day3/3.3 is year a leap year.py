# A year is a leap year if it's divisible by 4, except if it's evenly divisible by 100 UNLESS it is divisible
# by 400.
year = int(input("Please enter a year you want to check: "))
if year % 4 == 0:
    if year % 400 == 0:
        print("The year is a leap year")
    elif year % 100 == 0:
        print("The year is not a leap year")
    else:
        print("The year is a leap year!")
else:
    print("The year is not a leap year!")

