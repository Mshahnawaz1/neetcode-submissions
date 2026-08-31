# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        out = []
        q = collections.deque()
        q.append(root)
        out.append(root.val)
        while q:
            L = True #right not found
            for _ in range(len(q)):
                node = q.popleft()
                if node.right: 
                    q.append(node.right)
                    if L:
                        out.append(node.right.val)
                        L = False
                if node.left: 
                    q.append(node.left)
                    if L:
                        out.append(node.left.val)
                        L = False
        return out
