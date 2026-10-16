# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        prev, pnext = None, head
        curr = head

        while curr != None:
            
            pnext = curr.next
            curr.next = prev
            prev = curr
            curr = pnext

        return prev

            
            

