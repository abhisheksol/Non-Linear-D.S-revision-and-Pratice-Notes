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
        print(root.data, end=" ")
        inorder(root.right)

def search(root,key):
    if root is None or root.data==key:
        return root
    if root.data>key:
        return search(root.left,key)
    return search(root.right,key)


r=node(34)
r=insert(r,3)
r=insert(r,4)
r=insert(r,23)
r=insert(r,34)
r=insert(r,31)

inorder(r)
key=4

if search(r,key):
    print("it is found",key)
else:
    print("not found")


