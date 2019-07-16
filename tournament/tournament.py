from collections import defaultdict

results=defaultdict(dict)
def tally(rows):
    global results
    results = defaultdict(dict)
    for i in rows:
        temp=i.split(";")
        points(temp[0],'MP',1)
        points(temp[1], 'MP', 1)
        points(temp[0], 'P', 0)
        points(temp[1], 'P', 0)
        points(temp[0], 'W', 0)
        points(temp[1], 'W', 0)
        points(temp[0], 'D', 0)
        points(temp[1], 'D', 0)

        if temp[-1]=='win':
            points(temp[0],'W',1)
            points(temp[0],'P',3)

        elif temp[-1]=='draw':
            points(temp[1],'D',1)
            points(temp[0], 'D', 1)
            points(temp[1], 'P', 1)
            points(temp[0], 'P', 1)

        elif temp[-1]=='loss':
            points(temp[1],'W',1)
            points(temp[1],'P',3)

    tuple_results=tuple(results.items())
    tuple_results=sorted(tuple_results,key=lambda x:x[0])
    tuple_results = sorted(tuple_results, key=lambda x: x[1]['P'],reverse=True)

    output=['Team                           | MP |  W |  D |  L |  P']

    for i in tuple_results:
        s=""
        s+=i[0].ljust(31)
        loss=i[1]['MP']-(i[1]['W']+i[1]['D'])
        s+="|  "+str(i[1]['MP'])+" "+"|  "+str(i[1]['W'])+" "+"|  "+str(i[1]['D'])+" "+"|  "+str(loss)+" "+"|  "+str(i[1]['P'])
        output.append(s)

    return output

def points(player,result,value):
    global results
    if result not in results[player].keys():
        results[player][result] = value
    else:
        results[player][result] += value

