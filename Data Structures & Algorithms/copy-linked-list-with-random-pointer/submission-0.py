"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        has = {None:None}
        cur = head
        while(cur):
            new = Node(cur.val)
            has[cur] = new
            cur = cur.next
        cur = head
        while(cur):
            copy = has[cur]
            copy.next = has[cur.next]
            copy.random = has[cur.random]
            cur = cur.next
        return has[head]