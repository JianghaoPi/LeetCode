# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        k %= length
        if k == 0:
            return head
        k = length - k
        new_tail = head
        while k > 1:
            new_tail = new_tail.next
            k -= 1
        new_head = new_tail.next
        new_tail.next = None
        last.next = head
        return new_head
