#create node

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        # success greates inidival node with null

        # now we have to connect it 

class linkedlist:
    def __init__(self):
        self.head=None  #by default keep the head of node none if data is inserted or when it empty then it is usefull
    
    # now function for traversing
    def traversal(self):
        if self.head is None:
           print("linked is empty")
        n=self.head
        while n is not None:
            print(n.data)
            n=n.ref
        
    # now function to add node at the begining of the node 

    def add_beginning(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
ll=linkedlist()
ll.add_beginning(9)
ll.add_beginning(8)
ll.add_beginning(7)
ll.add_beginning(6)
ll.traversal()


    
    