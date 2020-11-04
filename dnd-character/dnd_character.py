from random import randint


class Character:
    
    def __init__(self):
        for stat in (
        'strength',
        'dexterity',
        'intelligence',
        'wisdom',
        'charisma',
        'constitution'):
            setattr(self, stat, self.ability())

        self.modifier = modifier(self.constitution) 
        self.hitpoints = 10 + self.modifier

    
    def ability(self):
        '''rolls four 6-sided dice and returns sum of largest three'''
        return sum(sorted([randint(1,6) for i in range(4)], reverse=True)[:3])


def modifier(constitution):
    return int((constitution - 10)//2)  

