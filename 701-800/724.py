"""
这一题看上去很简单,但是对于写python习惯了的人来说并不友好,因为内置的sum函数太好用了,就容易无脑开干
事实上,如果对每一个元素判断时都现场求和,这个时间开销也还是挺大的,只要每次判断不相等就把当前数字加进前半段的和里,
那么整个求和操作就从n平方变成n了
"""

import time


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        front_sum = 0
        for i in range(len(nums)):
            if front_sum * 2 == s-nums[i]:
                return i
            front_sum += nums[i]
        return -1


if __name__ == "__main__":
    sol = Solution()
    l = [0,1,0]
    start = time.time()
    print(sol.pivotIndex(l))
    print(time.time()-start)