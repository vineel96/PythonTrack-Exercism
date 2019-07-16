def distance(strand_a, strand_b):
    if len(strand_b)!=len(strand_a):
        raise ValueError("Unequal Length")
    else:
        nequal=[i!=j for i,j in zip(strand_a,strand_b)]
        return sum(nequal)