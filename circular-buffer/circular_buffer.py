class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None


class CircularBuffer(object):
    def __init__(self, capacity):
        self.buffer=linkedlist()
        self.capacity=capacity
        self.present_size=0


    def read(self):
        if self.present_size==0:
            raise BufferEmptyException(".+")
        else:
            data=self.buffer.head.data
            self.buffer.head=self.buffer.head.next
            self.present_size-=1
            return data


    def write(self, data):
        if self.buffer.head==None:
            self.buffer.head=Node(data)
            self.buffer.tail=self.buffer.head
            self.present_size+=1
        elif self.present_size==self.capacity:
           raise BufferFullException(".+")
        else:
            self.buffer.tail.next=Node(data)
            self.buffer.tail=self.buffer.tail.next
            self.present_size+=1


    def overwrite(self, data):
        if self.present_size!=self.capacity:
            self.buffer.tail.next=Node(data)
            self.buffer.tail=self.buffer.tail.next
            self.present_size+=1
        else:
            self.buffer.head=self.buffer.head.next
            self.buffer.tail.next=Node(data)
            self.buffer.tail=self.buffer.tail.next


    def clear(self):
        self.buffer = linkedlist()
        self.present_size = 0
