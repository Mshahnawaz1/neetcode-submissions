# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # has = set()
        # fast = head
        # while(curr.next):
        #     if curr in has:
        #         return True
        #     curr = curr.next
        # return False
        fast, slow = head, head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False