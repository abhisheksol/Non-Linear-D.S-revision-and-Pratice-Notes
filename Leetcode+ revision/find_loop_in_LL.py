class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self) -> None:
        self.start=None
    
    def insert_data(self):
        self.start=Node(1)
        first=Node(2)
        sec=Node(3)
        third=Node(4)
        fourth=Node(5)
        fiveth=Node(6)
        sixth=Node(7)
        self.start.next=first
        first.next=sec
        sec.next=third
        third.next=fourth
        fourth.next=fiveth
        fiveth.next=sixth
        # sixth.next=third
        sixth.next=None

    def detect_loop(self):
        first=self.start
        second=self.start.next
        # print(f"{first.data}:{second.data}")
        while first and second is not None:
            if first==second:
                return True
            first = first.next
            second = second.next.next
        print("no loop")
                

                # 
    # class Solution(object):
    # def hasCycle(self, head):
    #     fast = slow = head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #         if slow == fast:
    #             return True
    #     return False

    def traversal(self):
        while self.start is not None:
            print(self.start.data)
            self.start=self.start.next


        

l=linked_list()
l.insert_data()

l.detect_loop()
l.traversal()


    