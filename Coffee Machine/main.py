from data import *
import sys


def report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def get_payment():
    print("Please insert coins")
    return float(input("How many quarters: ")) * COINS["quarter"] + \
        float(input("How many dimes: ")) * COINS["dime"] + \
        float(input("How many nickels: ")) * COINS["nickel"] + \
        float(input("How many pennies: ")) * COINS["penny"]


def check_resources(coffee_type, resources, payment):
    for i in resources:
        if resources[i] < MENU[coffee_type]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
        elif payment < MENU[coffee_type]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False
        return True


def process(coffee_type, resources):
    payment = get_payment()
    if not check_resources(coffee_type, resources, payment):
        return resources
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    resources["money"] += payment - MENU[coffee_type]["cost"]   # Debug here
    print(f"Here is ${payment - MENU[coffee_type]['cost']} in change")
    print(f"Here is your ☕ {coffee_type}")
    return resources


def main(resources):
    ans = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ans in ('espresso', 'cappuccino', 'latte'):
        resources = process(ans, resources)
    elif ans == "report":
        report(resources)
    elif ans == "off":
        sys.exit()
    main(resources)


if __name__ == "__main__":
    main(RESOURCES)
