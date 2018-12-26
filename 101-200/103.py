
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        level = [root]
        while level:
            next_level = []
            i = len(level) - 1
            while i >= 0:
                cur = level[i]
                if cur.right:
                    next_level.append(cur.right)
                if cur.left:
                    next_level.append(cur.left)
                i -= 1
            if len(next_level) == 0:
                return res
            next_level_value = [node.val for node in next_level]
            res.append(next_level_value)
            level = next_level
            next_level = []
            i = len(level) - 1
            while i >= 0:
                cur = level[i]
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
                i -= 1
            if len(next_level) == 0:
                return res
            next_level_value = [node.val for node in next_level]
            res.append(next_level_value)
            level = next_level


