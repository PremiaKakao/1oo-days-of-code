# The goal of Day 2 is to make a Tip calculator that calculates how much each person has to pay
print("Welcome to the tip calculator")
total_bill = input("What was the total bill in dollars?")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15?")
number_of_people = input("How many people are splitting the bill?")

# Converting all the inputs to float and int
float_bill = float(total_bill[1:])
int_tip = int(tip_percentage)
int_people = int(number_of_people)


tip_in_decimals = 1 + int_tip/100
bill_with_tip = float_bill * tip_in_decimals
per_person = bill_with_tip / int_people
round_price = round(per_person, 2)

print(f"Each person should pay ${round_price}")
