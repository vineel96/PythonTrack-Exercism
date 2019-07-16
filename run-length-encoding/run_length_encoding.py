from collections import defaultdict
from itertools import groupby
import re
def decode(string):
    num=[int(n) if n else 1 for n in re.split('\D',string)]
    char="".join(n for n in re.split('\d',string) if n)
    return "".join([num*char for num, char in zip(num,char)])

def encode(string):
    out=""
    for char,group in groupby(string):
        l=len(list(group))
        if l>1:
            out+=str(l)+char
        else:
            out+=char
    return out