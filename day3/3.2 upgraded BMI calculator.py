# Upgraded BMI calculator will calculate the BMI of a person based on the input values and tell the user what their BMI
# says about their health

# Values input
height = float(input("Please enter your height: "))
weight = float(input("Please enter your height: "))

# BMI calculating
BMI = round(weight / height ** 2)

# Commenting on the BMI
if BMI < 18.5:
    comment = "underweight"
elif BMI < 25:
    comment = "normal weight"
elif BMI < 30:
    comment = "overweight"
elif BMI < 35:
    comment = "obese"
else:
    comment = "clinically obese"

print(f"Your current BMI is {BMI}, you are {comment}")
