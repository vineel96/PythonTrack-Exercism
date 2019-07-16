class Luhn(object):
    def __init__(self, card_num):
        self.card_num=card_num

    def valid(self):
        import re
        self.card_num=self.card_num.replace(" ","")
        if len(self.card_num)<=1 or re.findall("[^0-9 ]",self.card_num):
            return False
        else:
            digits=re.findall("[0-9]",self.card_num)
            for i in range(len(digits)-2,-1,-2):
                double=2*int(digits[i])
                if double>9:
                    digits[i]=double-9
                else:
                    digits[i]=double
            sum=0
            print(digits)
            for i in digits:
                sum+=int(i)
            print(sum)
            if sum%10==0:
                return True
            else:
                return False

