# OOP

class PlayerCharacter:
    # Class Object Attribute
    # Static and exists for all objects
    membership = True

    # Constructor
    # Special Method (Initialization)
    # Dunder or Magic Method
    def __init__(self, name, age):
        # Regular attributes
        if (self.membership):
            self.name = name
            self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'My name is {self.name}')

    def power_attack(self, power_level):
        print(f'Attack with Power {power_level}')


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
