# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        level = [self]
        s = [[self.val]]
        while level:
            next_level = []
            for i in level:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            if next_level:
                next_level_value = [node.val for node in next_level]
                s.append(next_level_value)
            level = next_level
        return "%s" % s

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "[null]"
        from collections import deque
        record = deque()
        record.append(root)
        value_list = [str(root.val)]
        while len(record) > 0:
            node = record.popleft()
            left_node = node.left
            if left_node:
                value_list.append(str(left_node.val))
                record.append(left_node)
            else:
                value_list.append("null")
            right_node = node.right
            if right_node:
                value_list.append(str(right_node.val))
                record.append(right_node)
            else:
                value_list.append("null")
        return "[" + ",".join(value_list) + "]"


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        data_list = data.strip("[]").split(',')
        if len(data_list) == 0:
            return None
        if data_list[0] == "null":
            return None
        record = deque()
        root = TreeNode(int(data_list[0]))
        record.append(root)
        i = 1
        while i < len(data_list):
            if data_list[i] != "null":
                left_node = TreeNode(int(data_list[i]))
                record[0].left = left_node
                record.append(left_node)
            i += 1
            if data_list[i] != "null":
                right_node = TreeNode(int(data_list[i]))
                record[0].right = right_node
                record.append(right_node)
            i += 1
            record.popleft()
        return root


if __name__ == '__main__':
    codec = Codec()
    print(codec.deserialize("[1,2,3,null,null,4,5]"))