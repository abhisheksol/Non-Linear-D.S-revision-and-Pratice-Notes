class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# -----------------------------------------------------------

class Linked_lost:
    def __init__(self):
        self.start=None

    def insert_at_end(self,value):
        new_node=Node(value)
        if self.start is None:
            self.start=new_node
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.next=None

    def traversing(self):
        while self.start is not None:
            print(self.start.data)
            self.start=self.start.next


i=Linked_lost()
i.insert_at_end(1)
i.insert_at_end(2)
i.insert_at_end(3)
i.insert_at_end(4)

i.traversing()