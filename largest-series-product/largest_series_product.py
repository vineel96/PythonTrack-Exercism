import re
def largest_product(series, size):
    if size>len(series) or size<0 or re.findall(r'[a-zA-Z]',series):
        raise ValueError("Error")
    else:
        return max([ product(s) for s in [series[l:l+size] for l in range(len(series)-size+1)]])

def product(string):
    prod=1
    for i in string:
        prod*=int(i)
    return prod