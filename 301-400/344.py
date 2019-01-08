class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString("A man, a plan, a canal: Panama"))