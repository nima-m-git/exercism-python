


YACHT = lambda dice: yacht(dice)
def yacht(dice):
        for i in range(1,6):
            if dice.count(i) == 5:
                return 50
        return 0

ONES = lambda dice: dice.count(1)*1
TWOS = lambda dice: dice.count(2)*2
THREES = lambda dice: dice.count(3)*3
FOURS = lambda dice: dice.count(4)*4
FIVES = lambda dice: dice.count(5)*5
SIXES = lambda dice: dice.count(6)*6
FULL_HOUSE = lambda dice: full_house(dice)
def full_house(dice):
        dubs, trips = False, False
        for i in range(6):
            if dice.count(i) == 2:
                dubs = True
            if dice.count(i) == 3:
                trips = True
        if dubs and trips:
            return sum(dice)
        else:
            return 0
        
FOUR_OF_A_KIND = lambda dice: quads(dice)
def quads(dice):
        for i in range(1,7):
            if dice.count(i) >= 4:
                return i*4
        return 0
    
LITTLE_STRAIGHT = lambda dice: little_straight(dice)
 def little_straight(dice):
        for i in range(1,6):
            if i not in dice:
                return 0
        return 30
    
BIG_STRAIGHT = lambda dice: big_straight(dice)
 def big_straight(dice):
        for i in range(2,7):
            if i not in dice:
                return 0
        return 30

CHOICE = lambda dice: sum(dice)


def score(dice, category):
    #want category to refer to a function to calculate score,
        #with dice as an argument
    return category(dice)
