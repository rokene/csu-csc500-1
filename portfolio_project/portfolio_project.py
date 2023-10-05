#!/usr/bin/env python3

import argparse
from app import *

global_config = {
    'force_confirmation': False
}

def main(args):

    if args.force:
        print('!! warning: forcing confirmations !!')
        global_config['force_confirmation'] = True

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple shopping sim CLI")
    parser.add_argument('-f',
                        '--force',
                        action='store_true',
                        required=False,
                        help="This indicates to force all confirmation to yes.")
    
    args = parser.parse_args()
    main(args)
