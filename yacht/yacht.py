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

from collections import Counter
# Score categories.
# Change the values as you see fit.
YACHT = (lambda y: 50 if len(set(y))==1 else 0)
ONES = (lambda y :count(y,1))
TWOS = (lambda y :count(y,2))
THREES = (lambda y :count(y,3))
FOURS = (lambda y :count(y,4))
FIVES = (lambda y :count(y,5))
SIXES = (lambda y :count(y,6))
FULL_HOUSE = (lambda y: sum(y) if sorted(Counter(y).values())==[2,3] else 0)
FOUR_OF_A_KIND = (lambda y: four_of_kind(y))
LITTLE_STRAIGHT = (lambda y: 30 if sorted(y)==[1,2,3,4,5] else 0)
BIG_STRAIGHT = (lambda y: 30 if sorted(y)==[2,3,4,5,6] else 0)
CHOICE = (lambda y:sum(y))

def count(list,value):
    return value*(list.count(value))

def four_of_kind(list):
    counter=Counter(list)
    for i in counter.items():
        if i[1]>=4:
            return 4*i[0]
    return 0

def score(dice, category):
    return category(dice)

