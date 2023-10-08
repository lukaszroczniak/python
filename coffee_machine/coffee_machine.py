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


def sufficient_resources(order_resources):
    """True if order can be made."""
    is_enough = True
    for item in order_resources:
        if order_resources[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
        return is_enough


def coins():
    """Calculating cents to dollars."""
    print("Insert coins.")
    quarters = int(input("quarters: ")) * 0.25
    dimes = int(input("dimes: ")) * 0.10
    nickles = int(input("nickles: ")) * 0.05
    pennies = int(input("pennies: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def drink_purchase(money, cost):
    """True when sufficient funds."""
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is the change ${change}")
        global money_in_machine
        money_in_machine += cost
        return True
    else:
        print("Sorry that is not enough money. Returning money...")
        return False


def make_coffee(drink_name, order_ingredients):
    """Subtracting ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


money_in_machine = 0

is_on = True


while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"water: {resources['water']}ml"
              f"\nmilk: {resources['milk']}ml"
              f"\ncoffee: {resources['coffee']}g"
              f"\nmoney: ${money_in_machine}")
    else:
        drink = MENU[user_choice]
        if sufficient_resources(drink["ingredients"]):
            amount_paid = coins()
            if drink_purchase(amount_paid, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
