from data import MENU
from data import resources
import random

machine_status = "ON"
revenue = 0

def check_choice(choice):
    while (not choice == 'espresso' and
           not choice == 'latte' and
           not choice =='cappuccino' and
           not choice == 'off' and
           not choice == 'report'):
        print("You didn't type the option correctly")
        choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    return choice

# TODO Print report of all coffee machine resources
def print_report():
    for key in resources:
        if key == 'coffee':
            print(f"{key}: {resources[key]}g")
        else:
            print(f"{key}: {resources[key]}ml")
    print(f"money: ${revenue}")

# TODO Check resources sufficient
def check_resources(choice):
    for key in resources:
        if resources[key] < MENU[choice]['ingredients'][key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

#TODO Process and count coins
def count_coins():
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    amount = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return amount

#TODO Update resources
def update_resources(choice):
    for key in resources:
        resources[key] -= MENU[choice]['ingredients'][key]

while machine_status == "ON":
    user_choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    user_choice = check_choice(user_choice)
    if user_choice == 'off':
        machine_status = "OFF"
    elif user_choice == 'report':
        print_report()
    else:
        if check_resources(user_choice):
            print("Please insert coins.")
            money = count_coins()
            if money < MENU[user_choice]['cost']:
                print(f"Sorry ${money} is not enough money."
                      f" {user_choice} price: ${round((money - MENU[user_choice]['cost']),4)}. Money refunded.")
            elif money > MENU[user_choice]['cost']:
                print(f"Here is ${round((money - MENU[user_choice]['cost']),4)} dollars in change.")
                print(f"Here is your {user_choice} ☕️! Enjoy!❤️")
                revenue += MENU[user_choice]['cost']
                update_resources(user_choice)
            else:
                print(f"Here is your {user_choice} ☕️! Enjoy!❤️")
                revenue += MENU[user_choice]['cost']
                update_resources(user_choice)


