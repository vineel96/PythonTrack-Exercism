def is_isogram(string):
    dict = {}
    for i in string:
        if i.lower() in dict.keys():
            return False
        elif i != " " and i != "-":
            dict[i.lower()] = "random"
    return True

    '''using set
        string=string.lower().replace('-','').replace(' ','')
        return len(string)==len(set(string))'''


