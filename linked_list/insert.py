# =========================================== NODE =========================================================
class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None

# =========================================================================================================
        

class Linked_list:
    def __init__(self):
        self.start=None

    def Insert_at_end(self,value):
        newnode=Node(value)
        if self.start==None:
            self.start=newnode
        else:
            temp=self.start
            while temp.Next!=None:
                temp=temp.Next
            temp.Next=newnode
            newnode.Next=None

    def traversal(self):
        if self.start==None:
            print("it is empty")
        else:
            while self.start!=None:
                print(self.start.data)
                self.start=self.start.Next

i=Linked_list()
i.Insert_at_end(1)
i.Insert_at_end(2)
i.Insert_at_end(4)
i.Insert_at_end(3)

i.traversal()


        

