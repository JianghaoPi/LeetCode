class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        if nums[-1] < nums[-2]:
            return nums[-1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid


sol = Solution()
print(sol.findMin([4,5,6,7,0,1,2]))
