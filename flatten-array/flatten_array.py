def flatten(iterable):
    out=[]
    for i in iterable:
        if type(i)==list:
            out+=flatten(i)
        elif i!=None and i!=():
            out.append(i)
    return out
