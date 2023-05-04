# OOP

class PlayerCharacter:
    # Class Object Attribute
    # Static and exists for all objects
    membership = True

    # Constructor
    # Special Method (Initialization)
    # Dunder or Magic Method
    def __init__(self, name='anonymous', age=0):
        # Regular attributes
        if (age > 18):
            self.name = name
            self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'My name is {self.name}')

    def power_attack(self, power_level):
        print(f'Attack with Power {power_level}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @classmethod
    def age_generate(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def subtract_things(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Adi', 23)
player2 = PlayerCharacter('Druva', 21)
player1.attack = 50
player2.defense = 100

print(player1.name, player1.age, player1.attack)
print(player2.name, player2.age, player2.defense)

print(player1.membership)
print(player2.membership)

# help(list)
player1.shout()
player2.shout()

player1.power_attack(23)

player3 = PlayerCharacter('Tom', 34)

player3.shout()

print(player1.adding_things(2, 3))

print(PlayerCharacter.adding_things(3, 4))

player4 = PlayerCharacter.age_generate(10, 23)

player4.shout()

print(PlayerCharacter.subtract_things(3, 4))
