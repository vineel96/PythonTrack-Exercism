import re
def annotate(minefield):
    if len({len(i) for i in minefield})>1 or any([bool(re.search(r'[^ *]',i)) for i in minefield]):
        raise ValueError(".+")
    for i in range(len(minefield)):
        for j in range(len(minefield[i])):
            count=0
            if minefield[i][j]==" ":
                if j+1<len(minefield[i]) and minefield[i][j+1]=="*": count+=1
                if j-1>=0 and minefield[i][j-1]=="*": count+=1
                if i-1>=0 and minefield[i-1][j]=="*": count+=1
                if i-1>=0 and j+1<len(minefield[i-1]) and minefield[i-1][j+1]=="*": count+=1
                if i-1>= 0 and j-1>=0 and minefield[i-1][j-1] == "*": count += 1
                if i+1<len(minefield) and minefield[i+1][j]=="*": count+=1
                if i+1<len(minefield) and j+1<len(minefield[i+1]) and minefield[i+1][j+1]=="*":count+=1
                if i+1<len(minefield) and j-1>=0 and minefield[i+1][j-1] == "*": count += 1
                l=list(minefield[i])
                if count>0:l[j]=str(count)
                minefield[i]="".join(l)
    return minefield