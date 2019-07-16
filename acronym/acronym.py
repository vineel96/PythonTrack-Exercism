def abbreviate(words):
    import re
    list=re.findall("[a-zA-Z]+'*[a-zA-Z]|[a-zA-Z]",words)
    str=""
    for i in list:
        str+=i[0].upper()
    return str