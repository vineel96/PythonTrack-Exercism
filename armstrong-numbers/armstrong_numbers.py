def is_armstrong_number(number):
    digits=len(str(number))
    return number==sum([pow(int(i),digits) for i in str(number)])