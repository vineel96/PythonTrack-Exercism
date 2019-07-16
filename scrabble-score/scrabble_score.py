def score(word):
    dict={
        ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'):1,
        ('D','G'):2,
        ('B','C','M','P'):3,
        ('F','H','V','W','Y'):4,
        ('K'):5,
        ('J','X'):8,
        ('Q','Z'):10
    }
    score=0
    for i in word:
        for j in dict.keys():
            if i.upper() in j:
                score+=dict[j]
    return score
