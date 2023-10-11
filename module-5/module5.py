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

def calculatePoints(books_purchased):
    if books_purchased < 2:
        return 0
    elif books_purchased < 4:
        return 5
    elif books_purchased < 6:
        return 15
    elif books_purchased < 8:
        return 30
    elif books_purchased >= 8:
        return 60

def bookRewards():
    books_purchased = userInputInt("Enter the number of books you have purchased this month: ", 0, None)
    points_awarded = calculatePoints(books_purchased)
    print(f"You have been awarded {points_awarded} points for purchasing {books_purchased} books.")

def avgRainfall():
    years = userInputInt("Enter the number of years to calculate average: ", 1, None)
    total_rainfall = 0.0

    for year in range(1, years + 1):
        print(f"Year {year}")
        for month in range(1, 13):
            monthly_rainfall = userInputFloat(f"Enter the inches of rainfall for month {month}: ", 0, None)
            total_rainfall += monthly_rainfall

    num_months = years * 12
    average_rainfall = total_rainfall / num_months

    print(f"Number of months: {num_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month: {average_rainfall}")

def main(args):
    if args.part == 1:
        avgRainfall()
    if args.part == 2:
        bookRewards()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Part 1, calculate average rainfall over years. Part 2, book purchase reward points.")
    parser.add_argument('--part',
                        type=int,
                        choices=[1, 2],
                        required=True,
                        help="This indicates whether to run part 1 or part 2 of the module.")

    args = parser.parse_args()
    main(args)

