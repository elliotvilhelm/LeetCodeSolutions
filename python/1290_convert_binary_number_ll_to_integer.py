# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        p = head
        tail = None
        size = 0
        while p:
            p = p.next
            size += 1
        
        p = head
        res = 0
        while p:
            if p.val == 1:
                res += 2 ** (size-1)
            p = p.next
            size -= 1
        
        return res