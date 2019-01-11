class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target, 0, len(nums)-1)

    def binarySearch(self, nums, target, left, right):
        if left >= right:
            if nums[left] == target:
                return left
            else:
                return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binarySearch(nums, target, mid+1, right)
        else:
            return self.binarySearch(nums, target, left, mid-1)


sol = Solution()
print(sol.search([-1,0,3,5,9,12],13))
