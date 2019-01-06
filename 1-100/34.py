class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return res
        if nums[0] == target:
            res[0] = 0
        if nums[-1] == target:
            res[1] = len(nums) - 1
        if res[0] != -1 and res[1] != -1:
            return res
        start = self.findStart(nums, 0, len(nums)-1, target)
        end = self.findEnd(nums, 0, len(nums)-1, target)
        if res[0] == -1 and res[1] == -1:
            return [start, end]
        if res[0] != -1:
            return [0, end]
        if res[1] != -1:
            return [start, res[1]]

    def findStart(self, nums, left, right, target):
        if left == right - 1:
            if nums[right] != target:
                return -1
            else:
                return right
        mid = (left + right) // 2
        if target <= nums[mid]:
            return self.findStart(nums, left, mid, target)
        else:
            return self.findStart(nums, mid, right, target)

    def findEnd(self, nums, left, right, target):
        if left == right - 1:
            if nums[left] != target:
                return -1
            else:
                return left
        mid = (left + right) // 2
        if target >= nums[mid]:
            return self.findEnd(nums, mid, right, target)
        else:
            return self.findEnd(nums, left, mid, target)


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([1,3], 1))