# THis code calculates and returns how many months, weeks and days the user has until they turn 90.
str_age = input("Please enter your age")

# Input works with strings only so we need to convert to int
age = int(str_age)

# Years until 90 
years = 90 - age

# A year has 12 months
months_until_90 = years * 12

# A year has 52 weeks
weeks_until_90 = years * 52

# A year is presumed to have 365 days, leap years are excluded
days_until_90 = years * 365

print(f"You have {days_until_90} days, {weeks_until_90} weeks and {months_until_90} months until 90")
