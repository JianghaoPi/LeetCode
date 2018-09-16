class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        res = ""
        i = 0
        if str[0] == "+" or str[0] == "-":
            res += str[0]
            i += 1
        while i < len(str):
            if "0" <= str[i] <= "9":
                res += str[i]
                i += 1
            else:
                break
        if res == "+" or res == "-" or res == "":
            return 0
        res = int(res)
        INT_MIN = -2 ** 31
        if res < INT_MIN:
            return INT_MIN
        INT_MAX = 2 ** 31 - 1
        if res > INT_MAX:
            return INT_MAX
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("words and 43"))
