# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nums = []
        self.getSum(root, 0, nums)
        res = 0
        for num in nums:
            res += num
        return res

    def getSum(self, root, pre, nums):
        num = pre*10 + root.val
        if not root.left and not root.right:
            nums.append(num)
            return
        if root.right:
            self.getSum(root.right, num, nums)
        if root.left:
            self.getSum(root.left, num, nums)
