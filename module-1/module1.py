#!/usr/bin/env python3

import argparse


def userInputFloat(message: str):
    while True:
        try:
            user_input=input(message)
            num=float(user_input)
            break
        except ValueError:
            print(f"'{user_input}' is not a valid number. Please try again.")
    return num

def main(args):
    num_one=None
    num_two=None
    result=None

    if not hasattr(args, 'number1'):
        num_one=userInputFloat("Please enter a number for the first number: ")
    else:
        num_one=args.number1

    print(f"For the first number you have entered: {num_one}")

    if not hasattr(args, 'number2'):
        num_two=userInputFloat("Please enter a number for the second number: ")
    else:
        num_two=args.number2

    print(f"For the second number you have entered: {num_two}")

    if args.type == "addition":
        print(f"Performing {args.type}: {num_one} + {num_two}")
        result = num_one + num_two
    elif args.type == "subtraction":
        print(f"Performing {args.type}: {num_one} - {num_two}")
        result = num_one - num_two
    elif args.type == "multiplication":
        print(f"Performing {args.type}: {num_one} * {num_two}")
        result = num_one * num_two
    elif args.type == "division":
        print(f"Performing {args.type}: {num_one} / {num_two}")
        result = num_one / num_two

    print(f"Result({args.type}): {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Performs arithmetic on two numbers.")
    parser.add_argument('-t',
                        '--type', 
                        type=str, 
                        choices=["addition", "subtraction", "multiplication", "division"], 
                        required=True, 
                        help="This is the type of arithmetic operation to perform.")
    parser.add_argument('-n1',
                        '--number1',
                        type=float,
                        default=None,
                        help="First number to use in arithmetic operation.")
    parser.add_argument('-n2',
                        '--number2',
                        type=float,
                        default=None,
                        help="Second number to use in arithmetic operation.")

    args = parser.parse_args()
    main(args)
