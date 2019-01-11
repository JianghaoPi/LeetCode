
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.postOrder(root, res)
        return res

    def postOrder(self, root, res):
        for child in root.children:
            self.postOrder(child, res)
        res.append(root.val)
