# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right):
            if not node: return True
            # valid if left is bst, right is bst and current node is valid
            if not (left < node.val < right):
                return False
            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))

        return dfs(root, float('-inf'), float('inf'))