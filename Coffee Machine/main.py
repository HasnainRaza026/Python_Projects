"""
Imports the sys module for system-specific functions and parameters, such as exiting the program.
"""
import sys
from data import COINS, MENU, RESOURCES


def report(resources):
    """
    Prints the current status of resources (water, milk, coffee, and money) in the coffee machine.

    Parameters:
    resources (dict): A dictionary containing the current resource quantities.
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def get_payment():
    """
    Prompts the user to insert coins and calculates the total payment amount.

    Returns:
    float: The total payment amount based on the inserted coins.
    """
    print("Please insert coins")
    return float(input("How many quarters: ")) * COINS["quarter"] + \
        float(input("How many dimes: ")) * COINS["dime"] + \
        float(input("How many nickels: ")) * COINS["nickel"] + \
        float(input("How many pennies: ")) * COINS["penny"]


def check_resources(coffee_type, resources, payment):
    """
    Checks if the coffee machine has enough resources and if the payment is sufficient.

    Parameters:
    coffee_type (str): The type of coffee being ordered.
    resources (dict): A dictionary containing the current resource quantities.
    payment (float): The amount of money provided by the user.

    Returns:
    bool: True if resources are sufficient and payment is enough, False otherwise.
    """
    for i in resources:
        if resources[i] < MENU[coffee_type]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
        if payment < MENU[coffee_type]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            return False
        return True


def process(coffee_type, resources):
    """
    Handles the coffee order process by accepting the coffee type and resources as input.
    It prompts the user to insert coins, checks if the resources are sufficient, 
    and processes the order accordingly.

    Parameters:
    coffee_type (str): The type of coffee being ordered.
    resources (dict): A dictionary containing the current resource quantities.

    Returns:
    dict: The updated resource quantities after processing the order.
    """
    payment = get_payment()
    if not check_resources(coffee_type, resources, payment):
        return resources
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    resources["money"] += MENU[coffee_type]["cost"]
    print(f"Here is ${payment - MENU[coffee_type]['cost']} in change")
    print(f"Here is your ☕ {coffee_type}")
    return resources


def main(resources):
    """
    The main function acts as the entry point for the coffee machine program.
    It continuously prompts the user for their choice of coffee, processes the order,
    and updates the resources accordingly.

    Parameters:
    resources (dict): A dictionary containing the current resource quantities.

    Returns:
    None
    """
    ans = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ans in ('espresso', 'cappuccino', 'latte'):
        resources = process(ans, resources)
    elif ans == "report":
        report(resources)
    elif ans == "off":
        sys.exit()
    else:
        print("Coffee type is not recognized.")
    main(resources)


if __name__ == "__main__":
    main(RESOURCES)
