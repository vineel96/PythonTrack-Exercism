verse={
    1:("that lay in","the house that Jack built."),
    2:("that ate","the malt"),
    3:("that killed","the rat"),
    4:("that worried","the cat"),
    5:("that tossed","the dog"),
    6:("that milked" ,"the cow with the crumpled horn"),
    7:("that kissed","the maiden all forlorn"),
    8:("that married", "the man all tattered and torn"),
    9:("that woke","the priest all shaven and shorn"),
    10:("that kept","the rooster that crowed in the morn"),
    11:("that belonged to" ,"the farmer sowing his corn"),
    12:(None,"the horse and the hound and the horn")
}

def recite(start_verse, end_verse):
    result=[]
    for i in range(start_verse,end_verse+1):
        result.append(construct_verse(i))
    return result

def construct_verse(number):
    out=""
    for i in range(number,0,-1):
        if i==number:
            out+="This is "+verse[i][1]+" "
        else:
            out+=verse[i][0]+" "+verse[i][1]+" "
    return out[:-1]