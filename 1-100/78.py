class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[], [nums[0]]]
        pre_res = self.subsets(nums[:-1])
        result = pre_res.copy()
        for i in pre_res:
            result.append(i + [nums[-1]])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2]))