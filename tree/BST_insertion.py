class node:
    def __init__(self,data):
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
            root.right= insert(root.right,value)
        else:
            root.left= insert(root.left,value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

r = node(50)
r=insert(r,60)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)
   