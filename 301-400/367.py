class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        return self.sqrt(num, 0, num)

    def sqrt(self, num, left, right):
        if left == right - 1:
            if left * left == num or right * right == num:
                return True
            else:
                return False
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        if mid * mid < num:
            return self.sqrt(num, mid, right)
        else:
            return self.sqrt(num, left, mid)
