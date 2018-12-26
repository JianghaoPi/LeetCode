class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums]
        pre_res = self.permute(nums[:-1])
        result = []
        for i in pre_res:
            for j in range(len(i)+1):
                b = i.copy()
                b.insert(j, nums[-1])
                result.append(b)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3]))