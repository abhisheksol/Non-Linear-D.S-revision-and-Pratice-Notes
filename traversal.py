# create node

class Node:
    def __init__(self,data) :
        self.data=data
        self.ref=None
        # created inidival empty linked list

# Now traversing them

class Linkedlist:
    def __init__(self):
       self.head=None
    #    by default head la None tavcha 

    def traversal(self):
        if self.head is None:
            print("linked is empty")
        n=self.head
        while n is not None:
            print(n.data)
            n=n.ref

# Adding the data to linked list at the begining 

    def add_begining(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

ll=Linkedlist()
ll.add_begining(5)
ll.add_begining(6)
ll.add_begining(7)
ll.traversal()

        