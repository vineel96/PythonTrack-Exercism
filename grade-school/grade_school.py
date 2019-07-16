class School(object):
    def __init__(self):
        self.database={}

    def add_student(self, name, grade):
        if grade in self.database.keys():
            self.database[grade].append(name)
            self.database[grade].sort()
        else:
            self.database[grade]=[name]

    def roster(self):
        list=sorted(self.database.keys())
        out=[]
        for grade in list:
            for name in self.database[grade]:
                out.append(name)
        return out

    def grade(self, grade_number):
        if grade_number in self.database.keys():
            return self.database[grade_number]
        else:
            return []
