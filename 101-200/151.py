class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        return " ".join(re.split('\s+', s.strip())[::-1])

    def reverseWords1(self, s):
        l = []
        word = ""
        i = 0
        while i < len(s):
            if s[i] != " ":
                word += s[i]
            if s[i] == " " or i == len(s) - 1:
                if word != "":
                    l.append(word)
                word = ""
            i += 1
        res = ""
        for j in range(len(l)-1, -1, -1):
            res += l[j] + " "
        return res[:-1]


sol = Solution()
print(sol.reverseWords1("the sky is blue"))