"""
思路：逆向往内圈写比较麻烦，可以考虑从内往外写，写完后用n**2+1减去所有元素，即为所求
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[]]
        reverse = self.generateReversedMatrix(n)
        for i in range(n):
            for j in range(n):
                reverse[i][j] = n**2 + 1 - reverse[i][j]
        return reverse

    def generateReversedMatrix(self, n):
        if n == 1:
            return [[1]]
        if n == 2:
            return [[4, 3], [1, 2]]
        inner_matrix = self.generateReversedMatrix(n-2)
        result = [[0] * n]
        for line in inner_matrix:
            result.append([0] + line + [0])
        result.append([0] * n)
        start = (n-2) ** 2 + 1
        for i in range(1, n):
            result[i][0] = start
            result[-1][i] = start + n - 1
            result[n-1-i][-1] = start + (n - 1) * 2
            result[0][n-1-i] = start + (n - 1) * 3
            start += 1
        return result
