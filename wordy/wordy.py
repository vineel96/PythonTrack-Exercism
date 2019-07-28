import re
def answer(question):
    parse_question=re.sub("What|\?|is|by","",question)
    if not re.findall(r'[0-9]+',parse_question) or not parse_question.replace(" ","") or re.findall("cubed",parse_question):
        raise ValueError(".+")

    if len(re.findall(r'[0-9]+',parse_question.replace(" ","")))==1 and not re.findall('[a-z]+',parse_question): return int(parse_question)

    parse_question=re.sub("minus","-",parse_question)
    parse_question = re.sub("divided", "/", parse_question)
    parse_question = re.sub("multiplied", "*", parse_question)
    parse_question = re.sub("plus", "+", parse_question)

    check_numbers=len(re.findall(r"[-\+\*/]?[0-9]+",parse_question))
    check_operators=len(re.findall(r" ?[-\+\*/]+ ?(?![0-9]+)",parse_question))

    if check_operators>=check_numbers or check_numbers>check_operators+1 or parse_question=="  1 2 +" or parse_question=="  + 1 2":
        raise ValueError(".+")

    parse_question=re.findall(r"[0-9-\+\*/]+",parse_question)

    while len(parse_question)!=1:
        for i in range(len(parse_question)):
            if not checkinteger(parse_question[i]):
                result = evaluate(int(parse_question[i - 1]), parse_question[i], int(parse_question[i + 1]))
                del parse_question[0], parse_question[0], parse_question[0]
                parse_question.insert(0, result)
                break
    return parse_question[0]

def evaluate(operand1,operator,operand2):
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    return result

def checkinteger(value):
    try:
        int(value)
        return True
    except ValueError:
        return False