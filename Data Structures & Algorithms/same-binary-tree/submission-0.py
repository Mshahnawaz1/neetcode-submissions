# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # q1 = collections.deque()
        # q2 = collections.deque()
        # q1.append(p)
        # q2.append(q)
        # while q1 and q2:
        #     n1, n2 = q1.popleft(), q2.popleft()
        #     if n1.val != n2.val:
        #         return False
        #     if n1.left and n2.left:
        if not p and not q:
            return True
        if (not p and q) or (p and not q) or p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right

