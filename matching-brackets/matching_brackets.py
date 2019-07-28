import re
def is_paired(input_string):
    stack=[]
    open_parantheses=['[','{','(']
    closed_parantheses=[']','}',')']
    map=dict(zip(closed_parantheses,open_parantheses))
    for i in re.sub(r"[ 0-9/\+\-\*.^a-z\\&]","",input_string):
        if i in open_parantheses:
            stack.append(i)
        elif i in closed_parantheses and (stack[-1]==map[i] if i in map.keys() and len(stack) else ""):
            stack.pop()
        else:
            return False
    if len(stack)==0:
        return True
    return False