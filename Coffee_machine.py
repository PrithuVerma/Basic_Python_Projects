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

on = True
profit = 0

def suff(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f'Sorry there is not enough {i} ')
            return False
        return True
    
def transaction(money_recieved , drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is you ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False
    
def bill():
    print("Please insert coins ")
    total = int(input('Enter number of quarters : ')) * 0.25
    total += int(input('Enter number of dimes : ')) * 0.1
    total += int(input('Enter number of nickles : ')) * 0.05
    total += int(input('Enter number of cents : ')) * 0.01
    return total

def make_coffee(drink_name , order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name} ☕️")

while on:
    order = input("What would you like? (espresso/latte/cappuccino):\nType 'report' for the report of ingredients \n ")
    if order == 'off':
        on = False
    elif order == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}ml")
        print(f"money : {profit}")
    else:
        drink = MENU[order]
        if suff(drink['ingredients']):
            payment = bill()
            if transaction(payment,drink["cost"]):
                make_coffee(order , drink["ingredients"])
