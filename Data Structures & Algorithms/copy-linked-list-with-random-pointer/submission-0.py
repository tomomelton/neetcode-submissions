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

        nodePairs = {None : None}

        node = head
        while node:
            nodePairs[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            nodePairs[node].next = nodePairs[node.next]
            nodePairs[node].random = nodePairs[node.random]
            node = node.next

        return nodePairs[head]