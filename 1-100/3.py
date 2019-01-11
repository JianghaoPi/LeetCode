"""
此题思路:
从前向后遍历,用字典保存遍历过的字母中离当前最近的索引,同时记录最近的一个不重复子串的起始索引和子串最大长度
当遇到重复字母后,更新起始索引,当发现当前位置离起始索引距离比已知最大子串更长的时候,更新最大长度
"""
import time


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        start = -1
        longest = 0
        for c in s:
            if c not in char_dict:
                char_dict[c] = -1
        for i in range(len(s)):
            start = max(start, char_dict[s[i]])
            longest = max(longest, i - start)
            char_dict[s[i]] = i
        return longest

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        refer = {}
        longest = 0
        start = -1
        for i in range(len(s)):
            if s[i] in refer:
                start = max(start, refer[s[i]])
            longest = max(longest, i - start)
            refer[s[i]] = i
        return longest

if __name__ == "__main__":
    sol = Solution()
    start = time.time()
    print(sol.lengthOfLongestSubstring2("abcabcbb"))
    print(time.time()-start)