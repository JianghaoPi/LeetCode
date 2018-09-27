"""
找出数组中不存在的最小正数.肯定就要先找出数组中的最大值了,如果最大值小于等于0,可以直接下结论是1了
如果最大值为正,那么就可以开一个MAX+2那么大的数组,记录下每一个正数,再遍历这个数组,找出最小正数
时间复杂度为n,空间复杂度为n
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        MAX = max(nums)
        if MAX <= 0:
            return 1
        record = [0] * (MAX + 2)
        for i in nums:
            if i > 0:
                record[i] = 1
        for j in range(1, MAX + 2):
            if record[j] == 0:
                return j


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([7,8,9,11,12]))