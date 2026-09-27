# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        node = head
        while node:
            if not node.next:
                return False
            elif node.next.val < node.val:
                return True
            node = node.next