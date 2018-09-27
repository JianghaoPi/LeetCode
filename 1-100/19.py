"""
此题让我想起了以前的快慢指针,用了差不多的算法,既然要删除倒数第n个节点,那么就弄两个指针,之间隔着n-2个节点即可,
先让指路指针走n-1步,然后处理指针指向头节点,再同步向后直到指路指针指向尾节点,达到n的时间复杂度.
只需注意处理好一些异常情况即可
"""

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
