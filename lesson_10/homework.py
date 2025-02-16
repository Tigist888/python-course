# Homework: Classes
# Read carefully until the end before you start solving the exercises.

# Practice the Basics

# Basic Class

# - Create an empty class HouseForSale
# - Create two instances.
# - Add number_of_rooms and price as instance attributes.
# - Create print statements that show the attribute values for the instances.

class HouseForSale:
    pass

# Creating two instances of the class
house1 = HouseForSale()
house2 = HouseForSale()

# Adding attributes dynamically
house1.number_of_rooms = 3
house1.price = 250000

house2.number_of_rooms = 4
house2.price = 350000

# Printing attribute values for both instances
print(f"House 1: {house1.number_of_rooms} rooms, Price: ${house1.price}")
print(f"House 2: {house2.number_of_rooms} rooms, Price: ${house2.price}")

#or
class HouseForSale:
    def __init__(self, number_of_rooms, price):
        self.number_of_rooms = number_of_rooms
        self.price = price
        print(f"House created: {self.number_of_rooms} rooms, Price: ${self.price}")

    def __str__(self):
        return f"House with {self.number_of_rooms} rooms, priced at ${self.price}"

# Creating instances
house1 = HouseForSale(3, 250000)
house2 = HouseForSale(4, 350000)

# Printing instances
print(house1)
print(house2)



# ----------------------------------------------------------------------------------------------------------------------

# Instance Methods

# - Create a Computer class.
# - Create method:
#   - turn_on that prints Computer has Turned On
#   - turn_off that prints Computer has Turned Off
# - Create an instance of the Computer class then call each method.

class Computer:
    def turn_on(self):
        print(" computer is turned on ")
    def turn_off(self):
        print("computer is truned off")
computer1=Computer()
computer1.turn_on()
computer1.turn_off()


# ----------------------------------------------------------------------------------------------------------------------

# Constructor with Parameters

# - Create a Dog class.
# - Dog should have a constructor with a name parameter.
# - Dog should have a method say_name that prints the name of the dog.

class Dog:
    def __init__(self,name):
        self.name=name
    def say_name(self):
        print(f"the name of the dog: {self.name}.")
dog=Dog("lulu")
dog.say_name()


# ----------------------------------------------------------------------------------------------------------------------

# Inheritance

# Create the classes that would make the following code possible, with the caveat that
# both Dog and Cat must inherit from Animal.
class Animal:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)  # Prints the animal's name

    def speak(self):
        print("I can't speak!")  # Corrected output with an exclamation mark


class Dog(Animal):
    def speak(self):
        print("Woof!")  # Dogs say "Woof!"


class Cat(Animal):
    def speak(self):
        print("Meow!")  # Cats say "Meow!"


dog = Dog('Fido')
dog.say_name()  # Prints: Fido
dog.speak()  # Prints: Woof!

cat = Cat('Max')
cat.say_name()  # Prints: Max
cat.speak()  # Prints: I can't speak!


class Dog(Animal):

dog = Dog('Fido')
dog.say_name()      # Prints: Fido
dog.speak()         # Prints: Woof!

cat =Cat('Max')
cat.say_name()      # Prints: Max
cat.speak()         # Prints: Meow!

# ----------------------------------------------------------------------------------------------------------------------

# Exercises
# Exercise 1: Books and Authors

# Create an empty class called Book. Then create three instances.
# Add the following attributes for each of the instances: title, author, and publication_year.
# Create print statements to display the attributes of each one of the instances.

# Pre-code:
class Book:
   pass

book1 = Book()
book1.titel = 'To Kill a Mockingbird'
book1.author = 'Harper Lee'
book1.publication = 1960

book2=Book()
book2.titel = 'The Great Gatsby'
book2.author = 'F. Scott Fitzgerald'
book2.publication = 1925


book3=Book()
book3.titel = 'Pride and Prejudice'
book3.author = 'Jane Austen'
book3.publication = 1813

print(f"book1:{book1.titel} by {book1.author},{book1.publication}")
print(f"book2:{book2.titel} by {book2.author},{book2.publication}")
print(f"book3:{book3.titel} by {book3.author},{book3.publication}")

# Your code here

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Vehicle and Types of Vehicles

# Create a Vehicle class.
# - Its constructor should take the name and type of the vehicle and store them as instance attributes.
# - This Vehicle class should also have a show_type() instance method that prints out the
#   message: "<NAME_OF_VEHICLE> is a <TYPE_OF_VEHICLE>"
# - Create Car and Bike classes that inherit from Vehicle.
# - Create instances of Car and Bike and make them show their types.
# Define the Vehicle class
class Vehicle:
    def __init__(self, name, vehicle_type):
        self.name = name
        self.vehicle_type = vehicle_type

    def show_type(self):
        print(f"{self.name} is a {self.vehicle_type}")


# Define the Car class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name, "Car")


# Define the Bike class that inherits from Vehicle
class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name, "Bike")


# Create instances of Car and Bike
car1 = Car("Toyota Corolla")
bike1 = Bike("Harley Davidson")

# Show their types
car1.show_type()
bike1.show_type()

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Spot and correct the mistakes

# - You are given a task to create a Car class.
# - Each car will have attributes for model and year.
# - Unfortunately, the given code below contains several mistakes.
# - Your task is to find and correct these mistakes to make the code run successfully.
# - Please include a comment in the code explaining the corrections you made and why.

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self):

        return f"Name of the car: {self.model}, Year: {self.year}"

my_car = Car("Toyota", 2014)

print(my_car)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. SmartHome with Constructor

# Create a SmartHome class that has a constructor __init__ and a send_notification() method.
#
# The constructor should initialize the attributes:
# - home_name
# - location
# - number_of_devices
#
# send_notification() should print a notification including the home_name and location.

# Create instances for the following:
# Home Name      Location      Number of Devices
# Villa Rosa     New York      15 devices
# Green House    California    10 devices
# Sea View       Florida       20 devices

# Call the send_notification() method for each instance,
# passing a message reminding to turn off the lights.

class SmartHome:
    def __init__(self, home_name, location, number_of_devices):
        self.home_name = home_name
        self.location = location
        self.number_of_devices = number_of_devices

    def send_notification(self, message):
        print(f"Notification for {self.home_name} in {self.location}: {message}")


# Creating instances for the homes
villa_rosa = SmartHome("Villa Rosa", "New York", 15)
green_house = SmartHome("Green House", "California", 10)
sea_view = SmartHome("Sea View", "Florida", 20)

# Sending notifications to each home
villa_rosa.send_notification("Reminder: Please turn off the lights.")
green_house.send_notification("Reminder: Please turn off the lights.")
sea_view.send_notification("Reminder: Please turn off the lights.")

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 5. Inheritance. Spot and correct mistakes

# You should have the following hierarchy of classes:

 # Animal
 # │
 # ├── Mammal
 # │
 # ├── Bird
 # │
 # └── Fish

# Each class has the following attributes:

# - Animal name
# - Mammal name, age, number of legs
# - Bird name, age, can fly or not
# - Fish name, age, number of fins

# But, the provided code for these classes and their instances has several mistakes
# related to hierarchy, class attributes, and instance creation.

# Find and correct these mistakes to make the code work properly.
# Leave a comment in the code explaining what the problems were and why it wouldn't work.
# There are seven mistakes in the pre-code.

# Pre-code
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mammal(Animal):
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

class Fish(Animal):
    def __init__(self, name, age, num_fins):
        super().__init__(name, age)
        self.num_fins = num_fins

# Instances
tiger = Mammal('Tiger', 5, 4)
sparrow = Bird('Sparrow', 2, True)
goldfish = Fish('Goldfish', 2, 'Many')