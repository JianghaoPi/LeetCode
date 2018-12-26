"""
贪心法，维护一个最大收益和最小价格，然后遍历，遇到更小的价格，更新最小价格，如果当前价格减去最小价格大于最大收益，更新最大收益
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        max_profit = 0
        record_min = prices[0]
        for i in prices:
            if i <= record_min:
                record_min = i
                continue
            if i - record_min > max_profit:
                max_profit = i - record_min
        return max_profit


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,6,4,3,1]))