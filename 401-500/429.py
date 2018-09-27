"""
树的层次遍历,先画出一棵树会比较好.看图说话
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[root.val]]
        if not root.children:
            return res
        level = [root]
        while True:
            next_level = []
            for node in level:
                if node.children:
                    next_level.extend(node.children)
            if next_level:
                level = next_level
                res.append(list(map(lambda x: x.val, next_level)))
            else:
                return res


if __name__ == "__main__":
    leaf1 = Node(7, [])
    leaf2 = Node(6, [])
    leaf3 = Node(5, [])
    leaf4 = Node(8, [])
    leaf5 = Node(9, [])
    leaf6 = Node(10, [])
    mid1 = Node(3, [leaf1, leaf2])
    mid2 = Node(2, [leaf3])
    mid3 = Node(4, [leaf4, leaf5, leaf6])
    root = Node(1, [mid1, mid2, mid3])
    sol = Solution()
    print(sol.levelOrder(root))