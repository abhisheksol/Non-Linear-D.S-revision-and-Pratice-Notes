class node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

def insert(root,value):
    if root is None:
        return node(value)
    else:
        if root.data==value:
            return root
        elif root.data<value:
            root.right=insert(root.right,value)
        else:
            root.left=insert(root.left,value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        preorder(root.right)
        print(root.data,end=" ")
        preorder(root.left)
        

r=node(85)
r=insert(r,45)
r=insert(r,34)
r=insert(r,56)
r=insert(r,76)
r=insert(r,34)
r=insert(r,23)

inorder(r)
print("------------------------------------")
preorder(r)



