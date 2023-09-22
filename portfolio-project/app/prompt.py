def userInputFloat(message: str):
    while True:
        try:
            user_input=input(message)
            num=float(user_input)
            break
        except ValueError:
            print(f"'{user_input}' is not a valid float. Please try again.")
    return num

def userConfirm(message: str):
    confirm=input(f"{message} (Y/N) ")

    if confirm == "Y" or confirm == "y":
        return True
    else:
        return False

def userInputStr(message: str):
    user_input = None
    while True:
        user_input=input(message)
        if userConfirm(f"Is this correct ({user_input})? "):
            break
    return user_input

def userInputInt(message: str):
    while True:
        try:
            user_input=input(message)
            num=int(user_input)
            break
        except ValueError:
            print(f"'{user_input}' is not a valid integer. Please try again.")
    return num
