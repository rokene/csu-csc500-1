#!/usr/bin/env python3

import argparse
from app import *

global_config = {
    'force_confirmation': False
}

def milestoneOne():
    items = []
    user_prompt = UserPrompt(global_config['force_confirmation'])
    num_items = 2

    print(f"Starting application. Please add {num_items} items.")

    for i in range(num_items):
        item_number = i + 1
        item_name = user_prompt.userInputStr(f"What is the name of item {item_number}? ")

        while any(item.item_name == item_name for item in items):
            print("That item name already exists. Please enter a unique name. These are the names tht exist: ")
            [print(item.item_name) for item in items]
            item_name = user_prompt.userInputStr(f"What is the name of item {item_number}? ")

        item_quantity = user_prompt.userInputInt(f"How many {item_name}(s) do you want to add? ", None, None)
        item_cost = user_prompt.userInputFloat(f"How much does each {item_name} cost? ", None, None)
        item = ItemToPurchase(item_name, item_cost, item_quantity)
        items.append(item)

    total_cost = 0.0
    total_items = 0
    print("Here is a list of your items:")
    for item in items:
        item.print_item_cost()
        total_cost += item.item_price * item.item_quantity
        total_items += item.item_quantity

    print(f"Total Cost: ${total_cost:.2f}")

def createItem(item_names_list, uniqueName=True, exitOnFail=False):
    user_prompt = UserPrompt(global_config['force_confirmation'])
    item_name = user_prompt.userInputStr(f"What is the name of item? ")

    if uniqueName:
        while any(name == item_name for name in item_names_list):
            print(f"The item name ({item_name}) already exists.")
            if exitOnFail:
                return None
            print(f"Please enter a unique name that are not the following: ")
            [print(name) for name in item_names_list]
            item_name = user_prompt.userInputStr(f"What is the name of item? ")
    else:
        while item_name not in item_names_list:
            print(f"The item name ({item_name}) does not exist.")
            if exitOnFail:
                return None
            print(f"Please enter a name that exists from the following: ")
            [print(name) for name in item_names_list]
            item_name = user_prompt.userInputStr(f"What is the name of item? ")

    item_quantity = user_prompt.userInputInt(f"How many {item_name}(s) do you want to add? ", 0, None)
    item_cost = user_prompt.userInputFloat(f"How much does each {item_name} cost? ", 0, None)
    item_description = user_prompt.userInputStr(f"What is the description of {item_name}? ")
    return ItemToPurchase(item_name, item_cost, item_quantity, item_description)

def printMenu(ShoppingCart):
    user_choice = ''
    user_prompt = UserPrompt(global_config['force_confirmation'])
    while user_choice != 'q':
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        user_choice = user_prompt.userInputStr("Choose an option:\n")
        item_names_list = [item.item_name for item in ShoppingCart.cart_items]

        if user_choice == 'a':
            item = createItem(item_names_list)
            if item:
                ShoppingCart.addItem(item)
            else:
                print(f'No item added to cart.')
        elif user_choice == 'r':
            if len(ShoppingCart.cart_items) <= 0:
                print("\nSHOPPING CART IS EMPTY")
            else:
                print("\nItems in cart:")
                [print(name) for name in item_names_list]
                name = user_prompt.userInputStr("Enter the item name:\n")
                ShoppingCart.removeItem(name)
        elif user_choice == 'c':
            if len(ShoppingCart.cart_items) <= 0:
                print("\nSHOPPING CART IS EMPTY")
            else:
                print("\nItems in cart:")
                [print(name) for name in item_names_list]
                item = createItem(item_names_list, False, True)
                if item:
                    ShoppingCart.modifyItem(item)
                else:
                    print(f'No item modified.')
        elif user_choice == 'i':
            ShoppingCart.printDescriptions()
        elif user_choice == 'o':
            ShoppingCart.printTotal()
        elif user_choice == 'q':
            break
        else:
            print(f"({user_choice}) is not a valid option!")

def milestoneTwo():
    user_prompt = UserPrompt(global_config['force_confirmation'])
    customer_name = user_prompt.userInputStr("Enter customer's name:\n")
    current_date = user_prompt.userInputStr("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date, global_config['force_confirmation'])
    printMenu(cart)

def main(args):
    if args.force:
        print('!! warning: forcing confirmations !!')
        global_config['force_confirmation'] = True

    if args.part == 1:
        milestoneOne()
    elif args.part == 2:
        milestoneTwo()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple shopping sim CLI")
    parser.add_argument('-f',
                        '--force',
                        action='store_true',
                        required=False,
                        help="This indicates to force all confirmation to yes.")
    parser.add_argument('--part',
                        type=int,
                        choices=[1, 2],
                        required=True,
                        help="This indicates whether to run part 1 or part 2 of the milestones.")
    args = parser.parse_args()
    main(args)
