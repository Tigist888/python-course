"""
Create an Animal class. Its constructor should take the name of the animal
and store it as an instance attribute. This Animal class should also have
a greeting() instance method that takes a name as an argument and prints
out the message: "Hello <NAME>, I'm <NAME_OF_ANIMAL>"

Create Dog and Cat classes that inherit from Animal.
Create instances and make them greet you.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def greeting(self, name):
        print(f"Hello! {name}, I am {self.name}")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog('Fido')
dog.greeting('John')


