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
    "money": 0,
}

def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${resources['money']}")

def calc_payment():
    quarters = int(input("Please insert coins.\nHow many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    pay_val = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return pay_val

def check_payment(drnk):
    """Checks if payment is valid. Returns 0 for no, 1 for yes, and 2 for change is owed."""
    valid_transaction = False
    payment = calc_payment()
    if payment >= drnk["cost"]:
        valid_transaction = True
        resources['money'] += drnk['cost']
        if payment > drnk['cost']:
            print(f"Here is ${payment - drnk['cost']} in change.")
    return valid_transaction

def main():
    still_running = True
    while still_running:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice.lower() == "report":
                print_report()
        else:
            drink = MENU[choice]
            valid_payment = check_payment(drink)
            valid_resources = check_resources(drink)
            if not valid_payment:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                if valid_resources:
                    print(f"Here is your {drink}. Enjoy!")
                else:
                    print(f"Sorry there is not enough {}.")

                
            
main()