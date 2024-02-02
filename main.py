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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

worth_of_quarter = 0.25
worth_of_dime = 0.10
worth_of_nickel = 0.05
worth_of_penny = 0.01
money = 0.00


def verify_payment(coffee):
    print('Please insert coins.')
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    pennies = input("How many pennies?: ")
    total = float((int(quarters) * worth_of_quarter)
                  + (int(dimes) * worth_of_dime)
                  + (int(nickels) * worth_of_nickel)
                  + (int(pennies) * worth_of_penny))
    price = MENU[coffee]["cost"]
    if price <= total:
        change = total - price
        global money
        money += price
        print(f"Here is ${format(change, ".2f")} in change.")
        print(f"Here is your {coffee} ☕️ Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


def use_resources(coffee):
    global resources
    ingredients_needed = MENU[coffee]["ingredients"]

    for ingredient, quantity in ingredients_needed.items():
        if quantity > resources[ingredient]:
            print(f"Sorry, not enough {ingredient}.")
            return False

    for ingredient, quantity in ingredients_needed.items():
        resources[ingredient] -= quantity

    return True


shopping = True
while shopping:
    user_answer = input("What would you like? (espresso/latte/cappuccino/never mind): ")
    if user_answer == 'report':
        for resource in resources:
            if resource == "water" or resource == "milk":
                print(f"{resource.capitalize()}: {resources[resource]}ml")
            else:
                print(f"{resource.capitalize()}: {resources[resource]}g")
        print(f"Money: ${money}")
    elif user_answer == 'espresso':
        if use_resources("espresso"):
            verify_payment("espresso")
    elif user_answer == 'latte':
        if use_resources("latte"):
            verify_payment("latte")
    elif user_answer == 'cappuccino':
        if use_resources("cappuccino"):
            verify_payment("cappuccino")
    elif user_answer == 'never mind':
        print("Have a great day!")
        shopping = False
    else:
        print("That wasn't an option.\n Goodbye")
        shopping = False
