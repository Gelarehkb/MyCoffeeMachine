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

cash = 0


def check_stock(ask):
    """Check if resources are sufficient for the selected drink."""
    ingredients = MENU[ask]["ingredients"]
    for item, amount in ingredients.items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def deduct_resources(ask):
    """Deduct the resources for the selected drink."""
    ingredients = MENU[ask]["ingredients"]
    for item, amount in ingredients.items():
        resources[item] -= amount


def paid_coins(quarter, dime, nickle, pennie):
    """Calculate the total amount paid by the user."""
    return 0.25 * quarter + 0.10 * dime + 0.05 * nickle + 0.01 * pennie


while True:
    ask = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if ask == "off":
        break
    elif ask == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${round(cash, 2)}")
    elif ask in MENU:
        if not check_stock(ask):
            continue

        print(f"Please pay ${MENU[ask]['cost']}")
        try:
            quarter = int(input("How many quarters? "))
            dime = int(input("How many dimes? "))
            nickle = int(input("How many nickles? "))
            pennie = int(input("How many pennies? "))
        except ValueError:
            print("Invalid input! Transaction canceled.")
            continue

        paid = paid_coins(quarter, dime, nickle, pennie)

        if paid >= MENU[ask]['cost']:
            change = round(paid - MENU[ask]['cost'], 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            cash += MENU[ask]['cost']
            deduct_resources(ask)
            print(f"Here is your {ask}. Enjoy!")
        else:
            print("Sorry, that's not enough money. Money refunded.")
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
