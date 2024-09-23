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
    header('BUY')
    ITEMCODE = input("ITEMCODE   : ")
    
    item = find(ITEMCODE)
    if item:
        print(f"Description: {item['DESCRIPTION']} ")
        print(f"Price      : {item['PRICE']} ")
        try:
            qty = int(input("QTY        : "))
            if qty > 0:
                # Append to the global CART list
                CART.append({ 'ITEMCODE': ITEMCODE, 'DESCRIPTION': item['DESCRIPTION'], 'PRICE': item['PRICE'], 'QUANTITY': qty })
                print("-" * 20)
                #print(f"{qty} of {item['DESCRIPTION']} added to cart.")               
                total_price = float(item['PRICE']) * qty
                print(f"Total      : {total_price:.2f}")              
            else:
                print("Quantity must be greater than zero.")
        except ValueError:
            print("Invalid quantity entered.")
    else:
        print("Item not found!")

def display_cart() -> None:
    header('Show Cart')
    if not CART:
        print("Your cart is empty.")
    else:
        
        print(f"{'#':<1} {'ITEMCODE':<10} {'DESCRIPTION':<15} {'PRICE':<10} {'QTY':<10} {'TOTAL':<10}")
        print("-" * 60)
        total_amount = 0.0  # Initialize total amount
        total_items = 0 
        total_count = 1
        
        
        
        
        for item in CART:
            total_items += item['QUANTITY']
            total_price = float(item['PRICE']) * item['QUANTITY']
            print(f"{total_count:<1} {item['ITEMCODE']:<10} {item['DESCRIPTION']:<15} {item['PRICE']:<10} {item['QUANTITY']:<10} {total_price:<10.2f}")
            total_amount += total_price  # Add item total price to total amount
            total_count += 1
        print("-" * 60)
        print(f"                                            total: {total_amount:.2f}")  # Display the total amount



def find_items() -> None:  # Function to display available items
    header('Show items')
    if len(BUY) == 0:
        print("No items available.")
    else:
        print(f"{'ITEMCODE':<10} {'DESCRIPTION':<25} {'PRICE':<10}")
        print("-" * 60)
        for item in BUY:
            print(f"{item['ITEMCODE']:<10} {item['DESCRIPTION']:<25} {item['PRICE']:<10}")
        print("-" * 60)

def displaymenu() -> None:
    system('cls')
    print('-' * 5 + 'Main Menu' + '-' * 5)
    print('1. BUY')
    print('2. SHOW CART')
    print('3. SHOW ITEMS')
    print('0. Quit/End')
    print('-' * 21)

# def displaymenu()->None:
    # system('cls')
    # print('-'*5+'Main Menu'+'-'*5)
    # print('1. Add Student') # BUY
    # print('2. Find Student') #SHOW CART
    # print('3. Update Student')
    # print('4. Delete Student')
    # print('5. Display All Student') #SHOW ITEMS
    # print('0. Quit/End')
    # print('-'*21)    

def terminate() -> None: 
    print('Program Ends')

def main() -> None:
    option:int = -1
    while option != 0:
        displaymenu()
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
