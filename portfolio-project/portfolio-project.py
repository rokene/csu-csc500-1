#!/usr/bin/env python3

import argparse
from app import *

def main(args):

    print("Please add two items.")
    items = []
    num_items = 2
    iteration = 1

    while len(items) < num_items:
        item_name = userInputStr(f"What is the name of item {iteration}? ")
        item_quantity = userInputInt(f"How many {item_name}(s) do you want to add? ")
        item_cost = userInputFloat(f"How much does each {item_name} cost? ")
        item = ItemToPurchase(item_name, item_cost, item_quantity)
        items.append(item)
        iteration += 1

    total_cost = 0.0
    total_items = 0
    print("Here is a list of your items:")
    for item in items:
        item.print_item_cost()
        total_cost += item.item_price * item.item_quantity
        total_items += item.item_quantity

    print(f"Total Cost: {total_cost}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple shopping sim CLI")

    args = parser.parse_args()
    main(args)
