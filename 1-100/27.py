class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        for i in nums:
            if i != val:
                nums[idx] = i
        return idx
