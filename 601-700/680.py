class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True
        return self.isPalindrome(s)

    def isAbsolutePalindrome(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

    def isPalindrome(self, s):
        if self.isAbsolutePalindrome(s):
            return True
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return self.isAbsolutePalindrome(s[i:len(s)-1-i]) or self.isAbsolutePalindrome(s[i+1:len(s)-i])