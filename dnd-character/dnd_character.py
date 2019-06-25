import random

class Character:
    def __init__(self):
        self.strength = random.randint(3,18)
        self.dexterity = random.randint(3,18)
        self.constitution = random.randint(3,18)
        self.intelligence = random.randint(3,18)
        self.wisdom = random.randint(3,18)
        self.charisma = random.randint(3,18)

        self.hitpoint = 10 + int((self.constitution - 10) / 2)

    def __roll_dice(self):
        return random.randint(1,6)

if __name__ == "__main__":
    
    char = Character()
    # print (char.strength)
    # print (char.charisma)
    # print (char.constitution)
    # print (char.hitpoint)
    # print (char.hitpoint)
    