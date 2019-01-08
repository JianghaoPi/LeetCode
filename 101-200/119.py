"""
思路：根据组合数公式直接计算
"""
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        res = [1]
        for i in range(1, rowIndex//2+1):
            tmp = res[-1]*(rowIndex-i+1)//i
            res.append(tmp)
        if rowIndex % 2 == 0:
            res = res + res[:-1][::-1]
        else:
            res = res + res[::-1]
        return res


sol = Solution()
print(sol.getRow(5))
