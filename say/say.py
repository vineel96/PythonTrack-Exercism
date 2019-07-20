one =['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
ten = ['zero','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def say(number):
    if number<0 or number>=1000000000000:
        raise Exception("Error")
    if number<20:
        return one[number]
    elif number<100:
        tenth=int(number/10)
        rem=number%10
        return ten[tenth]+("-"+say(rem) if rem else "" )
    elif number<1000:
        hundred=int(number/100)
        rem=number%100
        return one[hundred]+" hundred"+(" and " +say(rem) if rem else "")
    elif number<1000000:
        thousand=int(number/1000)
        rem=number%1000
        return say(thousand)+" thousand"+ (" "+say(rem) if rem else "")
    elif number<1000000000:
        million=int(number/1e6)
        rem=int(number%1e6)
        return say(million)+" million"+ (" "+ say(rem) if rem else "")
    else:
        billion=int(number/1e9)
        rem=int(number%1e9)
        return say(billion)+ " billion"+(" "+ say(rem) if rem else "")



