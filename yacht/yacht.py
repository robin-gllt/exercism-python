"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


# !!! Didn't understand the instruction well, my logic is wrong, it doesn't pass all tests

def score(dice, category):

    if category == 11: # Choice 
        return sum(dice)

    if category < 7:  
        return dice.count(category) * int(category)
    else:       
        if dice.count(dice[0]) == 5:  #Yacht - all dices identicals
            return 50 if category == 12 else 0
        elif dice.count(dice[0]) == 4 or dice.count(dice[1]) == 4:
            if category != 8:
                return 0
            elif dice.count(dice[0]) == 4:
                return dice[0] * 4
            else: 
                return dice[1] * 4
        elif dice == [1,2,3,4,5]:
            return 30 if category == 9 else 0 
        elif dice == [2,3,4,5,6]:
            return 30 if category == 10 else 0
        #Four of a kind
        else:
            print (sorted(dice)[0])
            if (sorted(dice)[0] == sorted(dice)[2] and sorted(dice)[3] == sorted(dice)[4]) or (sorted(dice)[0] == sorted(dice)[1] and sorted(dice)[2] == sorted(dice)[3]):
                return sum(dice) if category == 8 else 0
        return 0



if __name__ == "__main__":
    print(score([3, 3, 3, 3, 3], FOUR_OF_A_KIND))


'''
SOLUTION FROM Other: 

YACHT = (lambda x: 50 if len(set(x)) == 1 else 0)
ONES = (lambda x: digits(x,1))
TWOS = (lambda x: digits(x,2))
THREES = (lambda x: digits(x,3))
FOURS = (lambda x: digits(x,4))
FIVES = (lambda x: digits(x,5))
SIXES =(lambda x: digits(x,6))
FULL_HOUSE = (lambda x: sum(x) if sorted(Counter(x).values()) == [2,3] else 0)
FOUR_OF_A_KIND = (lambda x: four_of_a_kind(x)) 
LITTLE_STRAIGHT = (lambda x: 30 if sorted(x) == [1,2,3,4,5] else 0)
BIG_STRAIGHT = (lambda x: 30 if sorted(x) == [2,3,4,5,6] else 0)
CHOICE = sum 

def digits(x, digit):
    return digit * x.count(digit)

def four_of_a_kind(x):
    four_times_elements = [dice for dice in set(x) if x.count(dice) >= 4]
    return 4*four_times_elements[0] if len(four_times_elements) > 0 else 0

def score(dice, category):
    return category(dice)
    
    
ALSO:
YACHT = lambda d: 50 if len(set(d)) == 1 else 0
ONES = lambda d: sum(x for x in d if x == 1)
TWOS = lambda d: sum(x for x in d if x == 2)
THREES = lambda d: sum(x for x in d if x == 3)
FOURS = lambda d: sum(x for x in d if x == 4)


FULL_HOUSE = lambda d: sum(d) if len(set(d)) == 2 and any(d.count(x) == 3 for x in set(d)) else 0

=> set on list return a list of uniques values


    
    
    '''
    