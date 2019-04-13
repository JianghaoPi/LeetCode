class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        if len(nums) == 2:
            return -1
        return self.findPeak(nums, 1, len(nums)-2)

    def findPeak(self, nums, left, right):
        if left >= right:
            if nums[left] > nums[left-1] and nums[left] > nums[left+1]:
                return left
            else:
                return -1
        mid = (left + right) // 2
        left_res = self.findPeak(nums, left, mid)
        right_res = self.findPeak(nums, mid+1, right)
        if left_res != -1:
            return left_res
        if right_res != -1:
            return right_res
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement([1,2,3,1]))