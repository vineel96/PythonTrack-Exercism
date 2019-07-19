def slices(series, length):
    i=0
    l=len(series)
    out=[]
    if length>l or length<=0:
        raise ValueError("Error")
    return [series[i:i+length] for i in range(l-length+1)]
