class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [l[0] for l in matrix]
        if len(matrix) == 2:
            return matrix[0] + matrix[1][::-1]
        if len(matrix[0]) == 2:
            res = [matrix[0][0]]
            for i in range(len(matrix)):
                res.append(matrix[i][1])
            for i in range(len(matrix)-1, 0, -1):
                res.append(matrix[i][0])
            return res
        result = matrix[0].copy()
        for i in range(1, len(matrix)):
            result.append(matrix[i][-1])
        result.extend(matrix[-1][-2::-1])
        for i in range(len(matrix)-2, 0, -1):
            result.append(matrix[i][0])
        inner_matrix = [line[1:-1] for line in matrix][1:-1]
        return result + self.spiralOrder(inner_matrix)


print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))