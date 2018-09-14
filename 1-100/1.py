"""
此题常规的方法是两重循环遍历,但是可以通过使用字典保存遍历过的结果,只需要一重循环即可
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in complement_dict:
                return [complement_dict[nums[i]], i]
            else:
                complement_dict[complement] = i


if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,4]
    target = 6
    print(sol.twoSum(nums, target))