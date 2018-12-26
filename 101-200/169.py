class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        record = {}
        threshold = len(nums) // 2
        for i in nums:
            if i in record:
                record[i] += 1
                if record[i] > threshold:
                    return i
            else:
                record[i] = 1
