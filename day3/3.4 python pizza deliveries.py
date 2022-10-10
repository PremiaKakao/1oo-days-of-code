# Let's presume the person cooperates and only inputs the allowed answers
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L?")
add_pepperoni = input("Do you want to add pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

# Current bill
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 2
else:
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your total bill is: ${bill}")