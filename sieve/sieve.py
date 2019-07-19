def primes(limit):
    list=[True for i in range(limit+1)]
    p=2
    print(list)
    while p*p<=limit:
        if list[p]==True:
            i=p*p
            while i<=limit:
                list[i]=False
                i+=p
        p+=1
    return [i for i in range(limit+1) if i>=2 and list[i]]