"""
题目描述的范围和实际不符
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [0] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if 0 <= key <= 1000000:
            self.hash[key] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if 0 <= key <= 1000000:
            self.hash[key] = 0

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if 0 <= key <= 1000000:
            return self.hash[key] == 1
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
