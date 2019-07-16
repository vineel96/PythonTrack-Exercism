import re
def response(hey_bob):
    parse_hey="".join(re.findall(r'[^ ]',hey_bob))
    if parse_hey=="" or not re.search('[a-zA-Z0-9?]',parse_hey):
        return 'Fine. Be that way!'
    elif parse_hey.isupper() and parse_hey[-1]=='?':
        return 'Calm down, I know what I\'m doing!'
    elif parse_hey[-1]=='?':
        return 'Sure.'
    elif parse_hey.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'

