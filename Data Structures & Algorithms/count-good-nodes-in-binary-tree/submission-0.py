# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodNodes(node, maxV):
            if not node: return 0

            res = 1 if node.val >= maxV else 0
            maxV = max(maxV, node.val)
            res += goodNodes(node.left, maxV)
            res += goodNodes(node.right, maxV)
            return res
            
        return goodNodes(root, root.val)