# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.get_mid(head)
        rev_head = self.reverse_list(mid.next)
        
        curr = head
        rev_curr = rev_head
        while rev_curr:
            if rev_curr.val != curr.val:
                return False
            curr = curr.next
            rev_curr = rev_curr.next
            
        return True
    
    
    def get_mid(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow
    
    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev