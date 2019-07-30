NODE, EDGE, ATTR = range(3)
from collections import defaultdict

class Node(object):
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=None):
        if type(data)!=list and data!=None:
            raise TypeError(".+")
        print(type(data))
        self.data=data
        self.nodes=[]
        self.edges=[]
        self.attrs=defaultdict()
        if self.data!=None:
            for i in self.data:
                if len(i)==0 or len(i)==1:
                    raise TypeError(".+")
                if (i[0]!=NODE and i[0]!=EDGE and i[0]!=ATTR):
                    raise ValueError(".+")
                if i[0] == NODE:
                    if len(i)>3 or len(i)<3:raise ValueError(".+")
                    self.nodes.append(Node(i[1], i[2]))
                elif i[0]==EDGE:
                    if len(i) > 4 or len(i) < 4: raise ValueError(".+")
                    self.edges.append(Edge(i[1],i[2],i[3]))
                elif i[0]==ATTR:
                    if len(i) > 3 or len(i) < 3: raise ValueError(".+")
                    self.attrs[i[1]]=i[2]
