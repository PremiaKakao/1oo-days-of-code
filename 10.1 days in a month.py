# Checks how many dahys are in a given month in a given year
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_a_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False
def how_many_days_in_a_month(year, month):
    if is_a_leap_year(year) and month == 2:
        return 29
    else:
        return days_in_months[month - 1]

test_year = int(input("Please enter desired year\n"))
test_month = int(input("Please enter desired month\n"))
test_days_in_a_month = how_many_days_in_a_month(test_year, test_month)
print(f"Month number {test_month} has {test_days_in_a_month} days in {test_year}!")