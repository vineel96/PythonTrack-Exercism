import string

def is_pangram(sentence):
    letters=string.ascii_lowercase
    s=set(sentence.lower())
    for i in letters:
        if i not in s:
            return False
    return True

