

# 10.7 Call print(hydrogen). In the definition of Element, change the name of the
# method dump to __str__, create a new hydrogen object, and call print(hydrogen)
# again.
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'name = {self.name}, symbol = {self.symbol}, number = {self.number}'

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)


# 10.8 Modify Element to make the attributes name, symbol, and number private. Define
# a getter property for each to return its value.
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)

# 10.9 Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one
# method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or
# 'campers' (Octothorpe). Create one object from each and print what it eats.
class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

print(bear.eats(), rabbit.eats(), octothorpe.eats())

# 10.10 Define these classes: Laser, Claw, and SmartPhone. Each has only one method:
# does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (Smart
# Phone). Then, define the class Robot that has one instance (object) of each of these.
# Define a does() method for the Robot that prints what its component objects do.
class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return f'{self.laser.does()}, {self.claw.does()}, {self.smartphone.does()}'

robot = Robot()
print(robot.does())