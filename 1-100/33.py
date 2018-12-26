class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1 and target != nums[0]:
            return -1
        if nums[-1] >= nums[0]:
            return self.searchUp(nums, 0, len(nums)-1, target)
        else:
            return self.searchV(nums, 0, len(nums)-1, target)

    def searchUp(self, nums, left, right, target):
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        mid = (left + right) // 2
        left_res = self.searchUp(nums, left, mid, target)
        right_res = self.searchUp(nums, mid+1, right, target)
        res = left_res
        if right_res != -1:
            res = right_res
        return res

    def searchV(self, nums, left, right, target):
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        mid = (left + right) // 2
        if nums[mid] < nums[left]:
            left_res = self.searchV(nums, left, mid, target)
            right_res = self.searchUp(nums, mid+1, right, target)
        else:
            left_res = self.searchUp(nums, left, mid, target)
            right_res = self.searchV(nums, mid+1, right, target)
        res = left_res
        if right_res != -1:
            res = right_res
        return res

    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[right] >= nums[left]:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] >= nums[left]:
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1



if __name__ == "__main__":
    sol = Solution()
    print(sol.binarySearch([3,1], 1))
