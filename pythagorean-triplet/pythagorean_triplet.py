def triplets_with_sum(number):
    triples=set()
    for a in range(1,int(number/3)+1):
        for b in range(a+1,int(number/2)+1):
            c=number-a-b
            if a+b+c==number and is_triplet((a,b,c)):
                triples.add((a,b,c))
    return triples

def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    if triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2:
        return True

    return False
