class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                carry = digits[i] // 10
                digits[i] = digits[i] % 10
            else:
                carry = 0
                break
        if carry > 0:
            digits = [carry] + digits
        return digits


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([9,9,9,9]))
