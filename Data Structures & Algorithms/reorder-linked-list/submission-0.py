# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        L2 = slow.next
        slow.next = None
        
        # reverse L2
        prev = None
        while(L2):
            tmp = L2.next
            L2.next = prev
            prev = L2
            L2 = tmp

        L1, L2 = head, prev
        # Merge both
        while(L2):
            tmp1, tmp2 = L1.next, L2.next
            L1.next = L2
            L2.next = tmp1
            L1, L2 = tmp1, tmp2
