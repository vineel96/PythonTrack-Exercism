def translate(text):
    return ' '.join(transform(word)+'ay' for word in text.split(' '))

def transform(word):
    if word[0] in {'a','e','i','o','u'} or word[:2]=='xr' or word[:2]=='yt':
        return word
    elif word[:2]=='qu':
        return word[2:]+'qu'
    else:
        return transform(word[1:]+word[0]) if word[1]!='y' else word[1:]+word[0]