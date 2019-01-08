
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is not None:
            self.flattenChild(head)
        return head

    def flattenChild(self, head):
        cur = head
        while cur.next and not cur.child:
            cur = cur.next
        if not cur.child and not cur.next:
            return cur
        if cur.child and not cur.next:
            cur.next = cur.child
            cur.next.prev = cur
            cur.child = None
            return self.flattenChild(cur.next)
        if cur.child and cur.next:
            child_head = cur.child
            child_tail = self.flattenChild(child_head)
            cur.next.prev = child_tail
            child_tail.next = cur.next
            cur.next = child_head
            child_head.prev = cur
            cur.child = None
            return self.flattenChild(child_tail.next)
