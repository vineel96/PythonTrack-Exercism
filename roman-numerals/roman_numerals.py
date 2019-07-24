'''ten={   0:"",
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7:'VII',
        8:'VIII',
        9: 'IX',
        10: 'X'}
def roman(number):
    if number<=10:
        return ten[number]
    elif number<20:
        return 'X'+ten[number%10]
    elif number<40:
        num=int(number/10)
        rem=number%10
        return 'X'*num+ten[rem]
    elif number<50:
        return 'XL'+ten[number%10]
    elif number<90:
        num=int(number/10)
        rem=number%10
        return 'L'+'X'*(num-5)+ten[rem]
    elif  number<100:
        return 'XC'+ten[number%10]
    elif number<140:
        return 'C'+'X'*(int(number/10)%10)+ten[number%10]
    elif number<150:
        return 'C'+'XL'+ten[number%10]
    elif number<200:
        return 'CL'+'X'*((int(number/10)%10)-5)+ten[number%10]
    elif number>400 and number<500:
        return 'CD'+ten[number%10]
    elif number<900:
        return 'D'*((int(number/100))-4)+roman(number%100)
    elif number<1000:
        return 'CM'+roman(number%100)
    elif number<=3000:
        return 'M'*(int(number/1000))+roman(number%1000)'''

roman_numbers =[( 'M',  1000 ), ( 'CM',  900 ),( 'D',   500 ), ( 'CD',  400 ),( 'C',   100 ),
                ( 'XC',   90 ),( 'L',    50 ), ( 'XL',   40 ),
                ( 'X',    10 ), ( 'IX',    9 ),
                ( 'V',     5 ), ( 'IV',    4 ),
                ( 'I',     1 )]

def roman(number):
    out = ""
    for num, value in roman_numbers:
        while number >= value:
            out += num
            number -= value

    return out


