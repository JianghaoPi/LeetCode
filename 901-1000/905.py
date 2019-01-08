class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) == 0:
            return []
        left = 0
        right = len(A) - 1
        while left < right:
            while left < len(A) and A[left] % 2 == 0:
                left += 1
            while right >= 0 and A[right] % 2 == 1:
                right -= 1
            if left < right:
                A[left], A[right] = A[right], A[left]
        return A


sol = Solution()
print(sol.sortArrayByParity([3]))