def classify(number):
    if number<=0:
        raise ValueError(".+")
    else:
        factors=set()
        for i in range(1,int(pow(number,1/2))+1):
            if number%i==0:
                factors.add(i) if i!=number else ""
                factors.add(number/i) if (number/i)!=number else ""
        add=sum(factors)
        if add==number:
            return "perfect"
        elif add>number:
            return "abundant"
        else:
            return "deficient"
