# a simple cafeteria system
# gives a greeting based on real time
# store information such as emails and orders
from datetime import datetime

currently = datetime.now()
hour = currently.hour
#condition that reads and tells the greetings based on it time
if 0 <= hour < 12:
    print("Coffe Shops Good Morning!")
elif 12 <= hour < 18:
    print("Coffe Shops Good Afternoon!")
else:
    print("Coffe Shops Good Night!")
#Menu defined
menu = {
    "Sandwich": 2.50,
    "Coffe": 1.50,
    "Avocado smoothie": 3.50,
    "Strawberry Smoothie": 2.50,
    "Banana Smoothie": 1.50,
    "Cappucino": 1.00,
    "Arab Coffe": 5.00,
    "Milk Cinnamon flavored": 2.50,
    "Hot Chocolate":1.50,
    "Hot Chocolate Cinnamon Flavored": 2.00
    }
#To display the menu
def display_menu():
    print("Welcome to the Cafeteria!\nMenu:")
    for (item, price) in menu.items():
        print(f"- {item} - ${price:.2f}")
    print("Type '0' to Finish Order")

#Now the customer places an order
def take_orders():
    total = 0
    order_details = []

    while True:
        display_menu()
        choice = input("\nEnter the item number (or 0 to Finish): ")

        if choice == "0":
            break

        if choice in menu:
            item_name, item_price = menu[choice]

            try:
                quantity = int(input(f"How many {item_name}s would you like?"))
                if quantity <=0:
                    print("Quantity must be at least 1.")
                    continue
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue


            item_total = item_price * quantity
            total += item_total
            order_details.append((item_name, quantity, item_total))
            print(f"Added {quantity} x {item_name}(s) - ${item_total:.2f}")
        else:
            print("Invalid item number. Try again.")

    #Final receipt
    print("\nYour order summary:")
    for item_name, quantity, item_total in order_details:
        print(f"- {quantity} x {item_name}: $item_total:.2f")
    print(f"\nTotal to pay: ${total:.2f}")
    print("\nThank you for you order!")
#Run the program
take_orders()


