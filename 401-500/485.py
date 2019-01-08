class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        max_cnt = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            if nums[i] == 0:
                cnt = 0
            i += 1
        return max_cnt


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
