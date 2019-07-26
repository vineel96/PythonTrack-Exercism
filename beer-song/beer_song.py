def recite(start, take=1):
    song=[]
    while take!=0:
        if start==1:
            song.append("1 bottle of beer on the wall, 1 bottle of beer.")
            song.append("Take it down and pass it around, no more bottles of beer on the wall.")
        elif start==0:
            song.append("No more bottles of beer on the wall, no more bottles of beer.")
            song.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        else:
            song.append("{0} bottles of beer on the wall, {0} bottles of beer.".format(str(start)))
            song.append("Take one down and pass it around, {0} bottle{1} of beer on the wall.".format(str(start-1),("s" if (start-1)!=1 else "")))
        (song.append("") if take>1 else "")
        start-=1
        take-=1
    print(song)
    return song