#!/usr/bin/env python3

import argparse

force_confirmation=True

def userConfirm(message: str):

    if force_confirmation:
        return True

    confirm=input(f"{message} (To confirm: Y/y) ")

    if confirm == "Y" or confirm == "y":
        return True
    else:
        return False

def userInputStr(message: str, min: int, max: int):
    user_input = None
    while True:
        try:
            user_input=input(message)
            if min is not None and len(user_input) < min:
                raise ValueError(f'entered value is too short min is ({min})')
            if max is not None and len(user_input) > max:
                raise ValueError(f'entered value is too long max is ({max})')
            if userConfirm(f"Is this correct ({user_input})? "):
                break
        except ValueError as e:
            print(f"'{user_input}' is not a valid. ({e}) Please try again.")
    return user_input

def userInputFloat(message: str, min: float, max: float):
    while True:
        try:
            user_input=input(message)
            num=float(user_input)
            if min is not None and num < min:
                raise ValueError(f'entered value is less than min ({min})')
            if max is not None and num > max:
                raise ValueError(f'entered value is greater than max ({max})')
            if userConfirm(f"Is this correct ({user_input})? "):
                break
        except ValueError as e:
            print(f"'{user_input}' is not a valid number. ({e}) Please try again.")
    return num

def userInputInt(message: str, min: float, max: float):
    while True:
        try:
            user_input=input(message)
            num=int(user_input)
            if min is not None and num < min:
                raise ValueError(f'entered value is less than min ({min})')
            if max is not None and num > max:
                raise ValueError(f'entered value is greater than min ({max})')
            if userConfirm(f"Is this correct ({user_input})? "):
                break
        except ValueError as e:
            print(f"'{user_input}' is not a valid integer. ({e}) Please try again.")
    return num

def main(args):
    room_numbers = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }

    instructors = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }

    meeting_times = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }

    print('\nCourse List:')
    for course_name in room_numbers.keys():
        print(f'{course_name}')

    course_id = userInputStr("\nEnter a course number: ", None, None)

    course_id = course_id.upper()
    course_id = course_id.strip()

    if course_id in room_numbers.keys():
        print(f"\nCourse Number: {course_id}")
        print(f"Room Number: {room_numbers[course_id]}")
        print(f"Instructor: {instructors[course_id]}")
        print(f"Meeting Time: {meeting_times[course_id]}\n")
    else:
        print(f"\nSorry, course {course_id} is not in the system.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Course information finder.")
    args = parser.parse_args()
    main(args)
