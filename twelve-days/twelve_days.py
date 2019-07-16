dict = {
    1: ("first", "and a Partridge in a Pear Tree."),
    2: ("second", "two Turtle Doves"),
    3: ("third", "three French Hens"),
    4: ("fourth", "four Calling Birds"),
    5: ("fifth", "five Gold Rings"),
    6: ("sixth", "six Geese-a-Laying"),
    7: ("seventh", "seven Swans-a-Swimming"),
    8: ("eighth", "eight Maids-a-Milking"),
    9: ("ninth", "nine Ladies Dancing"),
    10: ("tenth", "ten Lords-a-Leaping"),
    11: ("eleventh", "eleven Pipers Piping"),
    12: ("twelfth", "twelve Drummers Drumming")
}

def recite(start_verse, end_verse):
    out=[]
    for i in range(start_verse,end_verse+1):
        out.append(form_verse(i))
    return out

def form_verse(index):
    str="On the "+dict[index][0] +" day of Christmas my true love gave to me: "
    for i in range(index,0,-1):
        str+=dict[i][1]+", "
    return str.replace("and ","").replace(", ","") if index==1 else str[:-2]