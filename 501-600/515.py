"""
层次遍历，每一层找到最大
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = [root.val]
        level = [root]
        while level:
            next_level = []
            level_max = None
            while level:
                cur = level.pop()
                if cur.right:
                    if level_max is None:
                        level_max = cur.right.val
                    elif cur.right.val > level_max:
                        level_max = cur.right.val
                    next_level.append(cur.right)
                if cur.left:
                    if level_max is None:
                        level_max = cur.left.val
                    elif cur.left.val > level_max:
                        level_max = cur.left.val
                    next_level.append(cur.left)
            level = next_level
            if level_max is not None:
                result.append(level_max)
        return result


sol = Solution()
root = TreeNode(1)
a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(5)
d = TreeNode(3)
e = TreeNode(9)
root.left = a


print(sol.largestValues(root))