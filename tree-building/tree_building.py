class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if records==[]:return None
    records=sorted(records,key=lambda x:x.record_id)
    tree=[]
    count=0
    for i in records:
        if i.parent_id not in [0]+[i for i in range(len(tree))] or count!=i.record_id:
            raise ValueError(".+")
        node=Node(count)
        tree.append(node)
        count+=1
        if i.record_id!=0:tree[i.parent_id].children.append(node)
    return tree[0]


