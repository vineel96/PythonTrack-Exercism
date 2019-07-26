secret={"wink":1,
"double blink":2,
"close your eyes":4,
"jump":8}

def commands(number):
    command=[]
    while number:
        if number & 1:
            command.append("wink")
            number=number ^ 1
        elif number & 2:
            command.append("double blink")
            number=number ^ 2
        elif number & 4:
            command.append("close your eyes")
            number=number ^ 4
        elif number & 8:
            command.append("jump")
            number=number ^ 8
        elif number & 16:
            command.reverse()
            number=number ^ 16

    return command


def secret_code(actions):
    code=[secret[i] for i in actions]
    number=0
    for  i in code:
        number=i^number
    return number^16 if sorted(code)!=code else number



