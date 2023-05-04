# OOP

class PlayerCharacter:
    # Constructor
    # Special Method (Initialization)
    # Dunder or Magic Method
    def __init__(self, name, age):
        # attributes
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Adi', 23)
player2 = PlayerCharacter('Druva', 21)
player1.attack = 50
player2.defense = 100

print(player1.name, player1.age, player1.attack)
print(player2.name, player2.age, player2.defense)

