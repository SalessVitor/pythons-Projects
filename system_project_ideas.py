# smart coffe machine
'''Concept: Build a terminal interface for a coffee machine.
Features:
Select coffee type (espresso, latte, americano)
Check water/milk/coffee levels
Refill supplies (simulate)
Start brewing (only if all ingredients are available)
Use while, if, break, and try/except for controls and input'''

import time
import sys


def looping_fake_loading(message="Preparing your drink", duration=5, delay=0.5):
    dots = ['', '.', '..', '...']
    end_time = time.time() + duration

    print(message, end='', flush=True)  # Print the message only once

    while time.time() < end_time:
        for dot in dots:
            sys.stdout.write(f'\r{message}{dot} ')
            sys.stdout.flush()
            time.sleep(delay)
    print()  # New line after the animation ends


def coffee_machine_interface():
    while True:

        print("\nCoffe machine")
        print("1 - Coffe")
        print("2 - Milk")
        print("3 - Hot chocolate")
        print("4 - Cancel Coffe")
        try:
            choice = int(input("Choose an option: "))
            if choice == 4:
                print("Cancelled")
                break
            elif choice == 1:
                bean = bean_types()
                drink_types(bean)
            elif choice == 2:
                milk_machine(choice)
            elif choice == 3:
                hot_chocolate(choice)
        except ValueError:
            print("Choose an option between 1-4")


def bean_types():
    print("1 - Arabica")
    print("2 - Robusta")
    print("3 - Excelsa")
    print("4 - Liberica")

    while True:
        try:
            bean = int(input("Select a Bean type (1-4): "))
            if bean in [1, 2, 3, 4]:
                return drink_types(bean)
            else:
                print("Invalid option. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        return bean_types()

def drink_types(bean):
    if bean:
        print("1 - Expresso")
        print("2 - Americano")
        print("3 - Capuccino")
        print("4 - Latte")
        print("5 - Machiatto")
        print("6 - Iced coffe")

        try:
            coffee = int(input("What type of drink 1-6: "))
            if coffee in [1, 2, 3, 4, 5, 6]:
                looping_fake_loading("Preparing your drink", duration=5, delay=0.5)
                print("Coffee served")
            else:
                print("Invalid input Please try a number between 1-6")
        except ValueError:
            print("Invalid input")
    return coffee_machine_interface()

def milk_machine(choice):
    if choice == 2:
        print("1 - Milk")
        print("2 - Coffee mixed with Milk")
        print("3 - Milk with cinnamon")
        print("4 - Sugar milk")
    while True:
        try:
            milk = int(input("What type of milk: "))
            if milk in [1,2,3,4]:
                looping_fake_loading("Preparing your milk", duration=5, delay=0.5)
                print("Milk served")
                break
            else:
                print("Invalid input Please try a number between 1-4")
        except ValueError:
            print("Invalid Input")


def hot_chocolate(choice):
    if choice == 3:
        print("1 - Hot chocolate")
        print("2 - Hot chocolate cinnamon flavored")

    while True:
        try:
            chocolate = int(input("What type of Hot chocolate: "))
            if chocolate in [1,2]:
                looping_fake_loading("Preparing your Hot chocolate", duration=5, delay=0.9)
                print("Hot chocolate served")
                break
            else:
                print("Invalid input Please try a number between 1-2")
        except ValueError:
            print("Invalid Input")



coffee_machine_interface()
