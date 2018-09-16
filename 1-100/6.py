class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        length = len(s)
        unit = 2 * (numRows - 1)
        a = length // unit
        b = length % unit
        if b > 0:
            a += 1
        res = s[::unit]
        for i in range(1, numRows - 1):
            start = 0
            while start <= a:
                if 0 < unit * start - i < length:
                    res += s[unit * start - i]
                if 0 < unit * start + i < length:
                    res += s[unit * start + i]
                start += 1
        for i in range(a):
            if i * unit + (numRows - 1) < length:
                res += s[i * unit + (numRows - 1)]
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 4))
