"""
这题比较基础,就是考察对链表的使用,主要分三步:
第一步,先无脑加到l1上,直到某一个链表到达尽头
第二步,判断l2是不是比较长的那个链表,如果是,就把l2后面多的部分接到l1后面
第三步,从头遍历l1,如果节点大于9,进行进位化简
最后处理一下异常情况,看最后一个节点是否大于9,如果是,新建一个节点接在后面
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = l1
        res = l1
        while True:
            l1.val = l1.val + l2.val
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
            else:
                break
        if l2.next:
            l1.next = l2.next
        while l3.next:
            record = l3.val
            l3.val = record % 10
            l3.next.val += record // 10
            l3 = l3.next
        if l3.val > 9:
            record = l3.val
            l3.val = record % 10
            l3.next = ListNode(record // 10)
        return res
