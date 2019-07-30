def transpose(lines):
    if not lines:
        return ""
    lines=lines.split("\n")
    length=len(max(lines,key=len))
    index=lines.index(max(lines,key=len))
    for i in range(len(lines)):
        if i!=index:
            lines[i]+="-"*(length-len(lines[i]))
    map=list(zip(*lines))
    result=[]
    for i in map:
        modify_value=modify(i)
        result.append("".join(modify_value))
    return "\n".join(result)


def modify(value):
    if "-" in value:
        l=list(value)
        index="".join(l).rindex("-")
        if index==len(l)-1:
            while l[index] == "-":
                l[index] = ""
                index -= 1
        for i in range(len(l)):
            if l[i]=="-":l[i]=" "
        return l
    return value