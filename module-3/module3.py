#!/usr/bin/env python3

import argparse


def userInputFloat(message: str, min: float, max: float):
    while True:
        try:
            user_input=input(message)
            num=float(user_input)
            if min is not None and num < min:
                raise ValueError(f'entered value is less than min ({min})')
            if max is not None and num > max:
                raise ValueError(f'entered value is greater than min ({max})')
            break
        except ValueError as e:
            print(f"'{user_input}' is not a valid number. ({e}) Please try again.")
    return num

def userInputInt(message: str, min: int, max: int):
    while True:
        try:
            user_input=input(message)
            num=int(user_input)
            if min is not None and num < min:
                raise ValueError(f'entered value is less than min ({min})')
            if max is not None and num > max:
                raise ValueError(f'entered value is greater than min ({max})')
            break
        except ValueError as e:
            print(f"'{user_input}' is not a valid number. ({e}) Please try again.")
    return num

def mealCalculator():
    subtotal = userInputFloat("How much was the subtotal for the food? $", 0, None)
    tip = subtotal * 0.18
    tax = subtotal * 0.07
    total = subtotal + tip + tax

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Sales Tax (7%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

def alarmCalculator():
    current_time = userInputInt("Enter the current time (0-23): ", 0, 23)
    wait_time = userInputInt("Enter the number of hours to wait for the alarm (0-n): ", 0, None)
    alarm_time = (current_time + wait_time) % 24
    print(f"The alarm will go off at: {alarm_time:02d}:00")

def main(args):
    if args.part == 1:
        mealCalculator()
    elif args.part == 2:
        alarmCalculator()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Part 1, meal cost calculator. Part 2, alarm clock calculator.")
    parser.add_argument('--part',
                        type=int,
                        choices=[1, 2],
                        required=True,
                        help="This indicates whether to run part 1 or part 2 of the module.")

    args = parser.parse_args()
    main(args)
