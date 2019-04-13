class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1 or n == 2:
            return True
        if n % 2 == 1:
            return False
        return self.isPowerOfTwo(n//2)

    def isPowerOfTwo2(self, n):
        if n <= 0:
            return False
        if n < 0:
            n = -n
        if n == 1 or n == 2:
            return True
        if n % 2 == 1:
            return False
        while n > 1:
            n = n // 2
            if n % 2 == 1:
                return False
        return True
