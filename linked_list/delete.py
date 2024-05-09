class node:
    def __init__(self,data) -> None:
        self.data=data
        self.Next=None

class linked_list:
    def __init__(self) -> None:
        self.start=None

    def insert_at_last(self,value):
        new_node=node(value)
        if self.start==None:
            self.start=new_node
        else:
            temp=self.start
            while temp.Next!=None:
                temp=temp.Next
            temp.Next=new_node
            new_node=None

    def delete_at_beginning(self):
        if self.start==None:
            print("it is empty")
        else:
            self.start=self.start.Next
    
    def traversal(self):
        if self.start==None:
            print("it is empty")
        else:
            while self.start!=None:
                print(self.start.data)
                self.start=self.start.Next

i=linked_list()
i.insert_at_last(5)
i.insert_at_last(4)
i.insert_at_last(65)
i.insert_at_last(8)
i.delete_at_beginning()

i.traversal()
        