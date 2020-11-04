# Score categories.
# Change the values as you see fit.

YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
##lambda dice: yacht(dice)
##def yacht(dice):
##        for i in range(1,6):
##            if dice.count(i) == 5:
##                return 50
##        return 0

ONES = lambda dice: dice.count(1)*1
TWOS = lambda dice: dice.count(2)*2
THREES = lambda dice: dice.count(3)*3
'''as an alternate example (FOURS), function of category name can be defined, passing
dice as an argument, and returning the function result. Lambda allows an argument to be
passed to its reference, and automatically returns the result'''
def FOURS(dice):
    return dice.count(4)*4

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

CHOICE = sum


def score(dice, category):
    return category(dice)





'''this was my first attempt; where the category name and score calculations
(passing dice as an argument, with more complex to an external function) are
stored in a dictionary, and the value calculated when retrieved. The category
name passed refers only to its string literal to be passed back through the
dictionary key to match, which seemed redundant/ugly.'''
##YACHT = 'YACHT'
##ONES = 'ONES'
##TWOS = 'TWOS'
##THREES = 'THREES'
##FOURS = 'FOURS'
##FIVES = 'FIVES'
##SIXES = 'SIXES'
##FULL_HOUSE = 'FULL_HOUSE'
##FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
##LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
##BIG_STRAIGHT = 'BIG_STRAIGHT'
##CHOICE = 'CHOICE'
##
##
##def score(dice, category):
##    kinds = {
##        'YACHT' : yacht(dice),
##        'ONES' : dice.count(1),
##        'TWOS' : dice.count(2) *2,
##        'THREES' : dice.count(3)*3,
##        'FOURS' : dice.count(4)*4,
##        'FIVES' : dice.count(5)*5,
##        'SIXES' : dice.count(6)*6,
##        'FULL_HOUSE' : full_house_score(dice),
##        'FOUR_OF_A_KIND' : quads_score(dice),
##        'LITTLE_STRAIGHT' : little_straight(dice),
##        'BIG_STRAIGHT' : big_straight(dice),
##        'CHOICE' : sum(dice),
##        }
##
##    return kinds[category]
