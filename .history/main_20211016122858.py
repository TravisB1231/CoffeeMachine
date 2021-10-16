# TODO 1. Print report of all coffee machine resources
# TODO 2. Check if resources sufficient to make drink order.
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

def calc_payment():    
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    pay_val = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return pay_val

def check_valid_amount():
    valid_transaction = False
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    drink = MENU[choice]
    payment = calc_payment()
    if drink["cost"] <= payment:
        valid_transaction = True
    return valid_transaction


valid_payment = check_valid_amount()
while valid_payment == False:
    print("Sorry that's not enough money. Money refunded.")
    check_valid_amount()