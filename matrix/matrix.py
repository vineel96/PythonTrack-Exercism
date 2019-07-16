class Matrix(object):
    def __init__(self, matrix_string):
        self.string=matrix_string

    def row(self, index):
        array = []
        l = []
        num = 0
        for i in self.string:
            if i != ' ' and i != '\n':
                num = num * 10 + int(i)
            if i == ' ':
                l.append(num)
                num = 0
            if i == '\n':
                l.append(num)
                num = 0
                array.append(l)
                l = []
        l.append(num)
        array.append(l)
        return array[index-1]


    def column(self, index):
        array=[]
        l=[]
        num=0
        for i in self.string:
            if i!=' ' and i!='\n':
                num=num*10+int(i)
            if i==' ':
                l.append(num)
                num=0
            if i=='\n':
                l.append(num)
                num=0
                array.append(l)
                l=[]
        l.append(num)
        array.append(l)
        print(array)
        col=[]
        for l in array:
            col.append(l[index-1])
            print(l)
        return col