# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

TARGET = 6

def guess(num):
    if num == TARGET:
        return 0
    if num > TARGET:
        return -1
    else:
        return 1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        left = 0
        right = n
        while left < right:
            if left == right - 1:
                if guess(left) == 0:
                    return left
                if guess(right) == 0:
                    return right
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                right = mid
            else:
                left = mid


sol = Solution()
print(sol.guessNumber(10))
