class Garden(object):
    dict={
        'G':"Grass",
        'C':"Clover",
        'R':"Radishes",
        'V':"Violets"
    }
    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David','Eve', 'Fred', 'Ginny', 'Harriet','Ileana', 'Joseph', 'Kincaid','Larry']):
        self.diagram=diagram
        self.students=sorted(students)

    def plants(self,name):
        index=0
        for i in range(len(self.students)):
            if name==self.students[i]:
               index=i
               break
        plant=self.diagram.split("\n")
        return " ".join([self.dict[p[index*2]]+" "+self.dict[p[index*2+1]] for p in plant]).split(" ")