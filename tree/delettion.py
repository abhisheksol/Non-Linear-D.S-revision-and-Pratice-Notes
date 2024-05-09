# ============================ Node ==========================================
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

# =============================================================================

def insert(root,value):
    if root is None:
        root=node(value)
    else:
        if root.data==value:
            return root
        elif root.data < value:
            root.right=insert(root.right,value)
        else:
            root.left=insert(root.left,value)
    return root

# =============================================================================


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

# =============================================================================

def delete(root,key):
    if root is None:
        return root
    else:
        if root.data==key:
            # 4conditions asnar ahe 
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                return root.left
            elif root.left is None and root.right is not None:
                return root.right
            else:
                store=root.right
                while store.left:
                    store=store.left
                root.data=store.data
                root.right=delete(root.right,store.data)

        elif root.data < key:
            root.right=delete(root.right,key)
        else:
            root.left=delete(root.left,key)
    return root




r=node(52)
r=insert(r,34)
r=insert(r,99)
r=insert(r,23)
r=insert(r,45)
r=insert(r,76)

key=45
inorder(r)
delete(r,key)
print("after deleting")
inorder(r)


