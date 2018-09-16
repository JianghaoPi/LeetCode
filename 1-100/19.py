# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        head = self
        res = ""
        while head.next:
            res += "%s -> " % head.val
            head = head.next
        res += str(head.val)
        return res


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        guide = head
        for i in range(n - 1):
            guide = guide.next
        if not guide.next:
            return head.next
        guide = guide.next
        target_prev = head
        while guide.next:
            guide = guide.next
            target_prev = target_prev.next
        target_prev.next = target_prev.next.next
        return head


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(sol.removeNthFromEnd(head, 5))
