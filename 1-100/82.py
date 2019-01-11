# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = []
        cur = self
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return " -> ".join(res)

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = self.deleteHeadDuplicates(head)
        if not new_head or not new_head.next:
            return new_head
        cur = new_head
        tmp = None
        while True:
            if cur and cur.next:
                if cur.val != cur.next.val:
                    tmp = cur
                    cur = cur.next
                else:
                    cur = self.deleteHeadDuplicates(cur)
                    tmp.next = cur
            else:
                return new_head

    def deleteHeadDuplicates(self, head):
        if not head or not head.next or head.val != head.next.val:
            return head
        cur = head
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        return self.deleteHeadDuplicates(cur.next)
