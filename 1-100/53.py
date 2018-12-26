"""
贪心法，线扫描如果是正数就开始计算和，每次计算更新最大和，直到和为负，放弃本次计算，遇到下一个正数再次开始计算
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] <= 0:
                if nums[i] > max_sum:
                    max_sum = nums[i]
                i += 1
            record_sum = 0
            while i < len(nums) and record_sum + nums[i] > 0:
                record_sum += nums[i]
                if record_sum > max_sum:
                    max_sum = record_sum
                i += 1
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2]))