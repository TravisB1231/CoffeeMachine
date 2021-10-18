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
Money = 0

def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\nMoney: ${Money}")

def calc_payment():
    quarters = int(input("Please insert coins.\nHow many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    pay_val = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return pay_val

def validate_payment(drnk):
    """Checks if payment is valid. Returns 0 for no, 1 for yes, and 2 for change is owed."""
    valid_transaction = False
    payment = calc_payment()
    if payment >= drnk["cost"]:
        valid_transaction = True
        resources['money'] += drnk['cost']
        if payment > drnk['cost']:
            print(f"Here is ${payment - drnk['cost']} in change.")
    return valid_transaction

def validate_resources(drnk):
    """Returns True if all resources are good. Otherwise it returns the insufficient resource name(s), 'water', 'milk', 'coffee'."""
    valid_resources = False
    low_ingredients = []
    for ingredient in resources:
        if drnk["ingredients"][ingredient] > resources[ingredient]:    
            low_ingredients.append(ingredient)
        

        
    return valid_resources

def main():
    still_running = True
    while still_running:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice.lower() == "report":
            print_report()
        elif choice.lower() == "exit"|"close"|"logout":
            print("Have a great day. Goodbye! :)")
            still_running = False
        elif choice == "espresso"| "latte" | "cappuccino":
            drink = MENU[choice]
            if validate_payment(drink):
                if validate_resources(drink):
                    print(f"Here is your {drink}. Enjoy!")
                #else:
                    #print(f"Sorry there is not enough {}.")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Invalid choice.")                
            
main()