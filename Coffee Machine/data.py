"""
Defines the MENU dictionary, which contains the details of each coffee type available.
Each coffee type is a key in the dictionary, with its corresponding value being another dictionary.
This inner dictionary contains two keys: 'ingredients' and 'cost'.

The 'ingredients' key maps to another dictionary, specifying the quantity of each ingredient.
The 'cost' key maps to a float value representing the cost of the coffee type.
"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


COINS = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}
