class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.q = [None] * k
        self.front = 0
        self.rear = 0
        self.length = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.length >= len(self.q):
            return False
        if self.length == 0:
            self.front = 0
            self.rear = 0
            self.q[0] = value
            self.length = 1
            return True
        if self.length < len(self.q):
            self.rear = (self.rear + 1) % len(self.q)
            self.q[self.rear] = value
            self.length += 1
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.length > 0:
            self.q[self.front] = None
            self.front = (self.front + 1) % len(self.q)
            self.length -= 1
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.length == 0:
            return -1
        return self.q[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.length == 0:
            return -1
        return self.q[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.length == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.length == len(self.q)

    def __str__(self):
        return "%s" % self.q

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj)
print(obj.enQueue(2))
print(obj)
print(obj.enQueue(3))
print(obj)
print(obj.deQueue())
print(obj)
print(obj.Front())
print(obj.Rear())
print(obj.isEmpty())
print(obj.isFull())
