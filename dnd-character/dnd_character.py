import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        rolls = [random.randint(1,6) for i in range(4)]
        return sum(sorted(rolls)[1:])
        


def modifier(constitution):
    return ((constitution - 10) // 2)


if __name__ == "__main__":
    
    char = Character()
    print (char.strength)
    # print (char.charisma)
    # print (char.constitution)
    # print (char.hitpoint)
    # print (char.hitpoint)
    