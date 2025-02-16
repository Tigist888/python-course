class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animals):
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, can_fly):
        self.can_fly = can_fly

class Fish(Mammal):
    def __init__(self, name, age, num_fins):
        super().__init__(name, age)
        self.num_fins = num_fins

tiger = Mammal('Tiger', 5, 4)
sparrow = Bird(True)
goldfish = Fish('Goldfish', 2, 'Many')