def factors(value):
    factors=[]
    while value%2==0:
        factors.append(2)
        value=value/2
    i=3
    while i<=pow(value,1/2):
        while value%i==0:
            factors.append(i)
            value=value/i
        i+=2
    if value>2:
        factors.append(value)
    return factors
