"""
该题要求将数组中的数字两两配对，然后使得所有对的较小数之和最大，就要让每一对的差最小，不然只取其中的较小值，较大那个就浪费了
所以先排序，然后相邻配对即可
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.quickSort(nums, 0, len(nums)-1)
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]
        return res

    def quickSort(self, nums, left, right):
        if left >= right:
            return
        i = left
        j = right
        pivot = nums[left]
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
        nums[i] = pivot
        self.quickSort(nums, left, i-1)
        self.quickSort(nums, i+1, right)


if __name__ == '__main__':
    sol = Solution()
    print(sol.arrayPairSum([1,4,3,2]))