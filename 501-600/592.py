"""
思路:
本题也属于比较基础,没有什么骚操作,干就完事了.
我用了两种方法,最开始面向对象,构造了分数类,实现了add方法和toString方法,然后用栈逆序存储表达式,不停计算化简,
但是很遗憾,这种方法只能打败30%的python对手,看来建新建对象开销还是太大了,但是我还是比较喜欢这种完备的方法
后来就很简单,直接上手处理,思路一样,估计还是越简单越光荣吧,这种没有任何亮点的方法打败了100%的对手
总结起来说,刷题这种东西和实际工程应用还是有很大不一样
"""

class Solution(object):
    def fractionAddition1(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        sign_dict = {"+": 1, "-": -1}
        exp_stack = list(expression)[::-1]
        if exp_stack[-1] != "-":
            exp_stack.append("+")
        res = Fraction(1, 0, 1)
        while exp_stack:
            sign = sign_dict[exp_stack.pop()]
            numerator = 0
            while exp_stack[-1] != "/":
                numerator = numerator * 10 + int(exp_stack.pop())
            exp_stack.pop()
            denominator = 0
            while exp_stack and "0" <= exp_stack[-1] <= "9":
                denominator = denominator * 10 + int(exp_stack.pop())
            tmp = Fraction(sign, numerator, denominator)
            res = res.add(tmp)
        return res.toString()

    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        sign_dict = {"+": 1, "-": -1}
        x = 0
        y = 1
        if expression[0] != "-":
            expression = "+" + expression
        i = 0
        while i < len(expression):
            sign = sign_dict[expression[i]]
            i += 1
            numerator = 0
            while expression[i] != "/":
                numerator = 10 * numerator + int(expression[i])
                i += 1
            i += 1
            denominator = 0
            while i < len(expression) and "0" <= expression[i] <= "9":
                denominator = 10 * denominator + int(expression[i])
                i += 1
            x = sign * numerator * y + x * denominator
            y = y * denominator
            for j in range(2, 10):
                while x % j == 0 and y % j == 0:
                    x = x // j
                    y = y // j
        return str(x) + "/" + str(y)


class Fraction(object):
    def __init__(self, sign, numerator, denominator):
        self.sign = sign
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        numerator = self.sign * self.numerator * other.denominator + self.denominator * other.numerator * other.sign
        if numerator == 0:
            return Fraction(1,0,1)
        sign = numerator // abs(numerator)
        numerator = abs(numerator)
        denominator = self.denominator * other.denominator
        for i in range(2, denominator):
            while numerator % i == 0 and denominator % i == 0:
                numerator = numerator // i
                denominator = denominator // i
        return Fraction(sign, numerator, denominator)

    def toString(self):
        fraction_str = "%s/%s" % (self.numerator, self.denominator)
        if self.sign == -1:
            fraction_str = "-" + fraction_str
        return fraction_str

if __name__ == "__main__":
    sol = Solution()
    print(sol.fractionAddition("-1/2+1/2"))
