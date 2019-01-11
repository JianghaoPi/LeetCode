# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        left = 1
        right = n
        while left < right:
            if right - left == 1 and not isBadVersion(left) and isBadVersion(right):
                return right
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
