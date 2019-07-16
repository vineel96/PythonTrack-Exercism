def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    first=-12345
    second=-12345
    third=-12345
    for i in scores:
        if i>first:
            third=second
            second=first
            first=i
        elif i>second:
            third=second
            second=i
        elif i>third:
            third=i
    if first!=-12345 and second!=-12345 and third!=-12345:
        return [first,second,third]
    elif first!=-12345 and second!=-12345:
        return [first,second]
    elif first!=-12345:
        return [first]
    else:
        return []
