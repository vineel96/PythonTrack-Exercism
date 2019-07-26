def largest(min_factor, max_factor):
    return find_palindrome(min_factor,max_factor,smallest=False)

def smallest(min_factor, max_factor):
    return find_palindrome(min_factor,max_factor)


def find_palindrome(min_factor,max_factor,smallest=True):
    if min_factor>max_factor or max_factor<min_factor:
        raise ValueError(".+")
    if smallest:
        step=1
        min=min_factor**2
        max=max_factor**2
    else:
        step=-1
        min=max_factor**2
        max=min_factor**2
    for i in range(min,max,step):
        if str(i)==str(i)[::-1] and any(min_factor<=i//j<=max_factor for j in range(min_factor,max_factor+1)if i%j==0 ):
            return i,find_factors(i,min_factor,max_factor)
    return None,[]

def find_factors(number,min_factor,max_factor):
    factors = []
    for i in range(min_factor,max_factor+1):
        if number % i == 0:
            factors.append([i, number // i]) if min_factor<=number//i<=max_factor else ""
    return factors