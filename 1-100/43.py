class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        to_be_sum = []
        for i in range(len(num1)):
            res = "0" * i
            carry = 0
            for j in range(len(num2)):
                tmp = int(num1[i]) * int(num2[j]) + carry
                res += str(tmp % 10)
                carry = tmp // 10
            if carry != 0:
                res += str(carry)[::-1]
            to_be_sum.append(res)
        result = to_be_sum[-1]
        for i in range(len(to_be_sum)-1):
            adder = to_be_sum[i]
            res = ""
            carry = 0
            for j in range(len(adder)):
                tmp = int(result[j]) + int(adder[j]) + carry
                res += str(tmp % 10)
                carry = tmp // 10
            idx = len(adder)
            while len(result) > idx and carry > 0:
                tmp = int(result[idx]) + carry
                res += str(tmp % 10)
                carry = tmp // 10
                idx += 1
            if carry > 0:
                res += str(carry)[::-1]
            res += result[idx:]
            result = res
        return result[::-1]

sol = Solution()
print(sol.multiply("123", "456"))