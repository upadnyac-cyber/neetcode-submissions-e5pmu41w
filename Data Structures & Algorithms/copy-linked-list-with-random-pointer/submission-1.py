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

        dummy = Node(0,head)
        copy = {None : None}

        while head:
            curr = Node(head.val)
            copy[head] = curr
            head = head.next
        
        head = dummy.next

        while head:
            curr = copy[head]
            curr.next = copy[head.next]
            curr.random = copy[head.random]
            head = head.next

        return copy[dummy.next]




        