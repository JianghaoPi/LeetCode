class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            if nums[i] != nums[res]:
                res += 1
                nums[res] = nums[i]
        return res + 1

