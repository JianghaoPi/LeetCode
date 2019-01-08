class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        record = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                tmp = []
                while record[-1] != '[':
                    tmp.append(record.pop())
                record.pop()
                num = []
                while record[-1].isdigit():
                    num.append(record.pop())
                    if len(record) == 0:
                        break
                record.append(int("".join(num[::-1])) * "".join(tmp[::-1]))
            else:
                record.append(s[i])
            i += 1
        return "".join(record)


if __name__ == '__main__':
    sol = Solution()
    print(sol.decodeString("10[leetcode]"))