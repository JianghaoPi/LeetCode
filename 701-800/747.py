class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        max1 = (nums[0], 0)
        max2 = (-float('inf'), -1)
        for i in range(len(nums)):
            if nums[i] > max1[0]:
                max2 = max1
                max1 = (nums[i], i)
            elif max2[0] < nums[i] < max1[0]:
                max2 = (nums[i], i)
        if max1[0] >= 2 * max2[0]:
            return max1[1]
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.dominantIndex([1]))
