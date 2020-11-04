from random import randint


class Character:
    
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.constitution = self.ability()
        self.modifier = modifier(self.constitution) 
        self.hitpoints = 10 + self.modifier

    
    def ability(self):
        '''rolls four 6-sided dice and returns sum of largest three'''
        return sum(sorted([randint(1,6) for i in range(4)], reverse=True)[:3])


def modifier(constitution):
    return int((constitution - 10)//2)
