# Student Project APP
from os import system
from studentapi import *
from data import BUY 

ITEMCODE:str = ""
DESCRIPTION:str = ""
PRICE:str = ""
CART:list = []  # List to hold cart items

def header(message) -> None:
    system('cls')
    print("-" * 20)
    print(message.upper().center(20))
    print("-" * 20)

def find(item_code: str) -> dict:
    """Find an item in the BUY list by ITEMCODE."""
    for item in BUY:
        if item['ITEMCODE'] == item_code:
            return item
    return None
        
def add() -> None:
    global ITEMCODE
    header('BUY ITEM')
    ITEMCODE = input("Enter ITEMCODE: ")
    
    item = find(ITEMCODE)
    if item:
        print(f"Description: {item['DESCRIPTION']}, Price: {item['PRICE']}")
        try:
            qty = int(input("Enter quantity: "))
            if qty > 0:
                # Append to the global CART list
                CART.append({'ITEMCODE': ITEMCODE, 'DESCRIPTION': item['DESCRIPTION'], 'PRICE': item['PRICE'], 'QUANTITY': qty})
                print(f"{qty} of {item['DESCRIPTION']} added to cart.")
            else:
                print("Quantity must be greater than zero.")
        except ValueError:
            print("Invalid quantity entered.")
    else:
        print("Item not found!")

def display_cart() -> None:
    header('CART CONTENT')
    if not CART:
        print("Your cart is empty.")
    else:
        print(f"{'ITEMCODE':<10} {'DESCRIPTION':<25} {'QUANTITY':<10} {'PRICE':<10}")
        print("-" * 50)
        for item in CART:
            total_price = float(item['PRICE']) * item['QUANTITY']
            print(f"{item['ITEMCODE']:<10} {item['DESCRIPTION']:<25} {item['QUANTITY']:<10} {total_price:<10.2f}")
        print("-" * 50)

def find_items() -> None:  # Function to display available items
    header('AVAILABLE ITEMS')
    if len(BUY) == 0:
        print("No items available.")
    else:
        print(f"{'ITEMCODE':<10} {'DESCRIPTION':<25} {'PRICE':<10}")
        print("-" * 50)
        for item in BUY:
            print(f"{item['ITEMCODE']:<10} {item['DESCRIPTION']:<25} {item['PRICE']:<10}")
        print("-" * 50)

def display_menu() -> None:
    system('cls')
    print('-' * 5 + 'Main Menu' + '-' * 5)
    print('1. BUY')
    print('2. SHOW CART')
    print('3. SHOW ITEMS')
    print('0. Quit/End')
    print('-' * 21)

def terminate() -> None: 
    print('Program Ends')

def main() -> None:
    option:int = -1
    while option != 0:
        display_menu()
        try:
            option = int(input('Enter Option (0..3): '))
            match option:
                case 1: add()  # Buy item
                case 2: display_cart()  # Show cart
                case 3: find_items()  # Show available items
                case 0: terminate()
                case _: print("Accept only 0 to 3")
        except Exception as e:
            print(f"Invalid Input: {e}")
        print()
        input("Press any key to continue...")

if __name__ == "__main__":
    main()