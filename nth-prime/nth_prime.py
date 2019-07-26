def nth_prime(number):
    if not number:
        raise ValueError(".+")
    count=0
    num=1
    while count<number:
        num+=1
        i=2
        isprime=True
        while i<=pow(num,1/2):
            if num%i==0:
                isprime=False
                break
            i=i+1
        if isprime:
            count+=1
    return num

