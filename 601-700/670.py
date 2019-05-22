'''
参考最大栈的方法，一个list保存逆序的数字，另一个list保存从末尾到当前为止最大的数及其所在位置
然后遍历二者直到第一个list中的数比第二个list记录的最大值小时，获得最大值位置，与其交换
'''

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = []
        max_num = []
        idx = 0
        while True:
            last = num % 10
            nums.append(last)
            if not max_num or max_num[-1][0] < last:
                max_num.append((last, idx))
            else:
                max_num.append(max_num[-1])
            if num > 9:
                idx += 1
                num //= 10
            else:
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < max_num[i][0]:
                nums[i], nums[max_num[i][1]] = nums[max_num[i][1]], nums[i]
                break
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            res = res * 10 + nums[i]
        return res


sol = Solution()
print(sol.maximumSwap(272))