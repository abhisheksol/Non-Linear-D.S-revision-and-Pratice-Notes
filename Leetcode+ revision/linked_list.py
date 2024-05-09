class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self) -> None:
        self.start=None
    
    def insert_data(self,value):
        new_node=Node(value)
        if self.start is None:
            self.start=new_node
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.next=None

    def traversal(self):
        while self.start is not None:
            print(self.start.data)
            self.start=self.start.next

    def reverse_traversal(self):
        head=self.start
        prev=None
        while head is not None:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        self.start=prev

        

l=linked_list()
l.insert_data(1)
l.insert_data(2)
l.insert_data(3)
l.insert_data(4)
l.reverse_traversal()
l.traversal()



    # def reverse_traversal(self):
    #     prev = None
    #     current = self.start
    #     while current is not None:
    #         temp = current.next
    #         current.next = prev
    #         prev = current
    #         current = temp
    #     self.start = prev