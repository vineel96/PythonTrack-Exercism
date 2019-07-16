def convert(number):
    div=[(3,"Pling"),(5,"Plang"),(7,"Plong")]
    string=[s for i,s in div if number%i==0]
    return "".join(string) if string else str(number)
