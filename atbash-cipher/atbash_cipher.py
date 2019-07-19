plain="abcdefghijklmnopqrstuvwxyz"
cipher="zyxwvutsrqponmlkjihgfedcba"
import string,re

trans=str.maketrans(plain,cipher)

def encode(plain_text):
    cipher_text=clean(plain_text).lower().translate(trans)
    return " ".join([cipher_text[i:i + 5] for i in range(0, len(cipher_text), 5)])



def decode(ciphered_text):
    return clean(ciphered_text).translate(trans)

def clean(text):
    return re.sub(r"[ ,@\'?\.$%!_]","",text)

