import string,re
def rotate(text, key):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    out=""
    lowercase=lowercase[key:]+lowercase[:key]
    uppercase = uppercase[key:] + uppercase[:key]
    for i in text:
        if re.match(r"[ ,@\'?\.$%!_0-9]",i):
            out+=i
        elif i.islower():
            out+=lowercase[ord(i)-97]
        elif i.isupper():
            out+=uppercase[ord(i)-65]
    return out
