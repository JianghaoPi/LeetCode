# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return [[""]]
        nodes = [[root.val]]
        m = 1
        level = [root]
        while 1:
            next_level = []
            for node in level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    next_level.extend([None, None])
            level = list(filter(lambda node: node, next_level))
            if len(level) == 0:
                break
            m += 1
            nodes.append([])
            for node in next_level:
                if node:
                    nodes[-1].append(node.val)
                else:
                    nodes[-1].append("")
            if len(list(filter(lambda node: node, next_level))) == 0:
                break
            level = next_level
        n = 2 ** m - 1
        res = []
        level_idx = [n // 2]
        all_idx = [n // 2]
        for i in range(m):
            level = [""] * n
            next_level_idx = [level_idx[0] // 2]
            for j in range(len(level_idx)):
                level[level_idx[j]] = str(nodes[i][j])
            for j in range(len(all_idx)):
                if j == len(all_idx) - 1:
                    next_level_idx.append((all_idx[j] + n) // 2)
                    break
                next_level_idx.append((all_idx[j] + all_idx[j+1])//2)
            all_idx = sorted(all_idx + next_level_idx)
            print(all_idx)
            level_idx = next_level_idx
            res.append(level)
        return res

root = TreeNode(3)
a = TreeNode(1)
b = TreeNode(5)
c = TreeNode(0)
d = TreeNode(2)
e = TreeNode(4)
f = TreeNode(6)
g = TreeNode(3)
root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
d.right = g
sol = Solution()
print(sol.printTree(root))
