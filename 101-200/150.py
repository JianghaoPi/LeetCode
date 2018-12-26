class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 0:
            return 0
        stack = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                res = int(eval("%s%s%s" % (a, i, b)))
                stack.append(res)
        return int(stack[-1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
