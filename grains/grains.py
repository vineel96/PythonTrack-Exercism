def square(number):
    if number < 1 or number > 64:
        raise ValueError("Error")
    return 1 << (number-1)

def total(number):
    if number < 1 or number > 64:
        raise ValueError("Error")
    return (1<<number) -1
