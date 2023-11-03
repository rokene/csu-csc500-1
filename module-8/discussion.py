#!/usr/bin/env python3

class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.__species = species

    def speak(self):
        pass

    def describe(self):
        return f"{self.__name} is a {self.__species}"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.__breed = breed

    def speak(self):
        return "Meow!"

    def describe(self):
        return f"{self._Animal__name} is a {self.__breed} cat"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.__breed = breed

    def speak(self):
        return "Woof!"

    def describe(self):
        return f"{self._Animal__name} is a {self.__breed} dog"


my_cat = Cat("Fluffy", "Persian")
my_dog = Dog("Buddy", "Golden Retriever")

print(my_cat.describe())
print(my_cat.speak())
print(my_dog.describe())
print(my_dog.speak())
