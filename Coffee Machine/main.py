from data import COINS, MENU, RESOURCES


def report(resources):
    """Prints the current resource status."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def get_payment():
    """Calculates the total payment amount from inserted coins."""
    print("Please insert coins")
    total = (float(input("How many quarters? ")) * COINS["quarter"] +
             float(input("How many dimes? ")) * COINS["dime"] +
             float(input("How many nickels? ")) * COINS["nickel"] +
             float(input("How many pennies? ")) * COINS["penny"])
    return total


def check_resources(coffee_type, resources, payment):
    """Checks if resources are sufficient and payment is enough."""
    for item, amount in MENU[coffee_type]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    if payment < MENU[coffee_type]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    return True


def process_order(coffee_type, resources):
    """Processes the coffee order."""
    payment = get_payment()
    if not check_resources(coffee_type, resources, payment):
        return resources
    for item, amount in MENU[coffee_type]["ingredients"].items():
        resources[item] -= amount
    resources["money"] += MENU[coffee_type]["cost"]
    change = payment - MENU[coffee_type]["cost"]
    print(f"Here is ${change:.2f} in change.")
    print(f"Here is your ☕ {coffee_type}. Enjoy!")
    return resources


def main():
    """Main function to run the coffee machine program."""
    resources = RESOURCES.copy()
    while True:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in MENU:
            resources = process_order(choice, resources)
        elif choice == "report":
            report(resources)
        elif choice == "off":
            break
        else:
            print(
                "Coffee type is not recognized. Please choose espresso, latte, or cappuccino.")


if __name__ == "__main__":
    main()
