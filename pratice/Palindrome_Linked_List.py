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
        temp=self.start
        while temp is not None:
            print(temp.data)
            temp=temp.next

    def palidrom(self):
        slow=fast=self.start
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        print(slow.data)

        stack1=[]
        stack2=[]
        fast=slow
        head=self.start
        while fast:
            stack1.append(fast.data)
            stack2.append(head.data)
            fast=fast.next
            head=head.next
        print(stack1)
        print(list(reversed(stack2)))
        stack2=list(reversed(stack2))
        if stack1==stack2:
            print("true")


        


i=Linked_lost()
i.insert_at_end(1)
i.insert_at_end(2)
i.insert_at_end(3)
# i.insert_at_end(2)
i.insert_at_end(2)
i.insert_at_end(1)

i.traversing()
print("--------------------")
i.palidrom()