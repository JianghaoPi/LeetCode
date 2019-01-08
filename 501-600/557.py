class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([x[::-1] for x in s.split(' ')])

sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))