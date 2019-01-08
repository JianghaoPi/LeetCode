class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if len(T) == 1:
            return [0]
        record = [(0, T[0])]
        res = [0] * len(T)
        for i in range(1, len(T)):
            while len(record) > 0 and T[i] > record[-1][-1]:
                tmp = record.pop()
                res[tmp[0]] = i - tmp[0]
            record.append((i, T[i]))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))