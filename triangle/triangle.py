def equilateral(sides):

    if len(set(sides))==1 and check(sides):
        return True
    return False


def isosceles(sides):
    if (len(set(sides))==1 or len(set(sides))==2) and check(sides):
        return True
    return False


def scalene(sides):
    if len(set(sides))==3 and check(sides):
        return True
    return False

def check(sides):
    if any(i<=0 for i in sides):
        return False
    if sides[0]+sides[1]>=sides[2] and sides[0]+sides[2]>=sides[1] and sides[1]+sides[2]>=sides[0]:
        return True
    return False