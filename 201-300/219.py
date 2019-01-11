class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if k <= 0:
            return False
        record = dict()
        for i in range(len(nums)):
            if nums[i] not in record or i - record[nums[i]] > k:
                record[nums[i]] = i
            else:
                return True
        return False


sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))
