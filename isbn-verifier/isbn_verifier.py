import re

def is_valid(isbn):
    parse_isbn=re.findall(r'[0-9X]',isbn)
    if len(parse_isbn)!=10:
        return False
    val=10
    result=0
    for i in parse_isbn:
        if i=='X':
            result+=10
        else:
            result+=val*int(i)
        val-=1
    return result%11==0