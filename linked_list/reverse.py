class node:
    def __init__(self,data):
        self.data=data
        self.Next=None

class linked_list:
    
    def __init__(self):
        self.start=None
    
    def insert_at_end(self,value):
        new_node=node(value)
        if self.start==None:
            self.start=new_node
        else:
            temp=self.start
            while temp.Next!=None:
                temp=temp.Next
            temp.Next=new_node
            new_node=None

    def traversal(self):
        if self.start==None:
            print("it is empty")
        else:
            while self.start!=None:
                print(self.start.data)
                self.start=self.start.Next

i=linked_list()
i.insert_at_end(3)
i.insert_at_end(8)
i.insert_at_end(7)

i.traversal()