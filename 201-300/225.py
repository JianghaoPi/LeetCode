from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.helper = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q) > 1:
            self.helper.append(self.q.popleft())
        res = self.q.popleft()
        self.q, self.helper = self.helper, self.q
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while len(self.q) > 0:
            res = self.q.popleft()
            self.helper.append(res)
        self.q, self.helper = self.helper, self.q
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0
