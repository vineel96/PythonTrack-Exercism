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

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST =0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if list_one==list_two:
        return EQUAL
    elif check(list_one,list_two):
        return SUBLIST
    elif check(list_two,list_one):
        return SUPERLIST
    else:
        return UNEQUAL

def check(a,b):
    l1,l2=len(a),len(b)
    return l1<l2 and any(b[i:i+l1]==a for i in range(l2))