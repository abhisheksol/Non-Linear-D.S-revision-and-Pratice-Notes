class node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

    def show(self):
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()

root=node(50)
left_node=node(30)
right_node=node(70)

root.left=left_node
root.right=right_node
root.show()