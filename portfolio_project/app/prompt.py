class UserPrompt:
    force_confirmation = False

    def __init__(
        self,
        force_confirmation):

        self.force_confirmation = force_confirmation

    def userConfirm(self, message: str):

        if self.force_confirmation:
            return True

        confirm=input(f"{message} (To confirm: Y/y) ")

        if confirm == "Y" or confirm == "y":
            return True
        else:
            return False

    def userInputStr(self, message: str):
        user_input = None
        while True:
            user_input=input(message)
            if self.userConfirm(f"Is this correct ({user_input})? "):
                break
        return user_input

    def userInputFloat(self, message: str, min: float, max: float):
        while True:
            try:
                user_input=input(message)
                num=float(user_input)
                if min is not None and num < min:
                    raise ValueError(f'entered value is less than min ({min})')
                if max is not None and num > max:
                    raise ValueError(f'entered value is greater than min ({max})')
                if self.userConfirm(f"Is this correct ({user_input})? "):
                    break
            except ValueError as e:
                print(f"'{user_input}' is not a valid number. ({e}) Please try again.")
        return num

    def userInputInt(self, message: str, min: float, max: float):
        while True:
            try:
                user_input=input(message)
                num=int(user_input)
                if min is not None and num < min:
                    raise ValueError(f'entered value is less than min ({min})')
                if max is not None and num > max:
                    raise ValueError(f'entered value is greater than min ({max})')
                if self.userConfirm(f"Is this correct ({user_input})? "):
                    break
            except ValueError as e:
                print(f"'{user_input}' is not a valid integer. ({e}) Please try again.")
        return num
