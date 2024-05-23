class node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LL:
    def __init__(self):
        self.start=None

    def insert(self,value):
        new_node=node(value)
        if self.start is None:
            self.start=new_node
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.next=None

    def traversal(self):
        temp=self.start
        while temp is not None:
            print(temp.data)
            temp=temp.next
    
    def reverse(self):
        current=self.start
        prev=None
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.start=prev


i=LL()
i.insert(1)
i.insert(2)
i.insert(3)
i.insert(4)
i.reverse()
i.traversal()