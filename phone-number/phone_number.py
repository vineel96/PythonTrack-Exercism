import re
class Phone(object):
    def __init__(self, phone_number):
        self.number=phone_number
        parse_number=re.sub(r'^(\+1)|[()-. ]',"",self.number)
        if (parse_number[0]=="1" and len(parse_number)==11):
            parse_number=re.sub(r'^1',"",parse_number)
        if len(parse_number)>10 or parse_number[0]=="1" or parse_number[0]=="0" or parse_number[3]=="1" or parse_number[3]=="0" or re.findall(r'[a-z]@:\!',parse_number):
            raise ValueError(".+")
        self.number=parse_number
        self.area_code=parse_number[:3]

    def pretty(self):
        return "("+self.number[:3]+")"+" "+self.number[3:6]+"-"+self.number[6:]

