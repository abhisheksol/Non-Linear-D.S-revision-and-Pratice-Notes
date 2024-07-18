# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if node is None:  # Check if node is None instead of root
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1  # Fix the balance condition and parentheses
            
            return [balanced, 1 + max(left[1], right[1])]
                        
        return dfs(root)[0]
#         1
#        / \
#       2   2
#      / \
#     3   3

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)


sol = Solution()
print(sol.isBalanced(root))  # Output: False
