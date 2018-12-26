class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        return self.sqrt(0, x, x)

    def sqrt(self, left, right, value):
        if right - left == 1 and left ** 2 <= value < right ** 2:
            return left
        mid = (right + left) // 2
        if mid ** 2 == value:
            return mid
        if mid ** 2 > value:
            return self.sqrt(left, mid, value)
        else:
            return self.sqrt(mid, right, value)
