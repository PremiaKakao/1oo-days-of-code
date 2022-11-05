#The coffe machine menu. Each item has its ingredeant list and price
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
#The value of the coins that may be inserted
money_value = {
    "quarters" : 0.25,
    "dimes" : 0.1,
    "nickles" : 0.05,
    "pennies" : 0.01
}
#Resources available for the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# reports back current resource quantity
def report():
    print(resources)
# uses resources
def use_resources(user_input):
    global resources
    used_resources = {key: resources[key] - MENU[user_input]["ingredients"].get(key, 0) for key in resources}
    return  used_resources
# checks if there's enough resources to make a drink
def is_there_enough_resources(resources_to_check):
    global resources
    failure_message = ''
    for k, v in resources_to_check.items():
        if v < 0:
            failure_message = f"There is not enough {k}"
            print(failure_message)
            return False
    if not failure_message:
        resources = resources_to_check
        return True
# propt user to give money
def user_gives_money():
    print("How are you to pay here for?")
    total_given_cash = 0
    for key, v in money_value.items():
        cash_value = int(input(f"How many {key} will you insert: \n"))
        total_given_cash += cash_value * v
    return  total_given_cash
# check if enough money is given and provide change
def is_it_enough_money(drink_cost, given_cash):
    if given_cash >= drink_cost:
        change = round(given_cash - drink_cost, 2)
        return change
    else:
        return False

turned_on = True
while turned_on:
    user_input = input("What would you like? (espresso/latte/cappuccino):\n")
    if user_input == "off":
        turned_on = False
    elif user_input == "report":
        report()
    elif user_input in MENU.keys():
        used_resources = use_resources(user_input)
        if is_there_enough_resources(used_resources):
            given_cash = user_gives_money()
            enough = is_it_enough_money(MENU[user_input]["cost"], given_cash)
            if not enough:
                print("Sorry that was not enough money! Money refunded")
            else:
                print(f"Thank you for your purchase! Your change is {enough} dollars")

        print(resources)
    else:
        print("Invalid")