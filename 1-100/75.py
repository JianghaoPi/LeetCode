"""
从前往后遍历，维护i和j两个指针，如果当前值为0，将其与i位交换，i向后走到不为0为止，j向前走到不为0为止，如果当前值为2，
将其与j位交换，i向后走到不为0为止，j向前走到不为0为止，
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        cur = 0
        while True:
            if nums[cur] == 0:
                nums[cur], nums[i] = nums[i], nums[cur]
                while i < len(nums) and nums[i] == 0:
                    i += 1
                while j >= 0 and nums[j] == 2:
                    j -= 1
                cur = i - 1
            if nums[cur] == 2:
                nums[cur], nums[j] = nums[j], nums[cur]
                while i < len(nums) and nums[i] == 0:
                    i += 1
                while j >= 0 and nums[j] == 2:
                    j -= 1
                cur = i - 1
            if cur == j:
                break
            cur += 1
        print(nums)

if __name__ == '__main__':
    sol = Solution()
    sol.sortColors([2, 0, 0])