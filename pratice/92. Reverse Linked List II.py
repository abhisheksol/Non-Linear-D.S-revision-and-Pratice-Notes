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
        l=3
        r=5
        dummy=node(0)
        dummy.next=self.start

        prev=dummy
        current=self.start
        for i in range(l-1):
            prev=prev.next
            current=current.next
        store_currents_position=current
        prev2=None
        for j in range(r-l+1):
            next=current.next
            current.next=prev2
            prev2=current
            current=next

        prev.next = prev2  # Corrected connection
        store_currents_position.next = current  # Corrected connection

        

        



i=LL()
i.insert(1)
i.insert(2)
i.insert(3)
i.insert(4)
i.insert(5)
i.insert(6)
i.reverse()
i.traversal()