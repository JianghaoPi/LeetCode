"""
本题思路比较简单,首先要满足的条件是所有汽油的量要大于等于路上消耗的量,否则不可能跑完全程
然后就是开始找一个起点,当某个点的汽油量足以支撑到下一个点时,认为可以开始.然后向后走,看能否走完全程,走不完就找到下一个可以开始的点继续.
但是这么暴力的遍历的话,时间复杂度是n^2,可以用合适的贪心算法去优化.
可以稍微想一想:如果从A走到B失败了,其实从A到A+1资源剩余是大于等于0的,那么从AB之间的任一点出发到B的资源更为紧张,所以从AB之间任一点出发都不可能到达B了,
接下来选定B作为起始点即可.这样大大减少了起始点的数量,也省了不少时间
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) - sum(cost) < 0:
            return -1
        l = len(gas)
        i = 0
        while i < l:
            if gas[i] - cost[i] >= 0:
                remain = 0
                j = 0
                start = i
                for j in range(i, i + l):
                    remain += (gas[j % l] - cost[j % l])
                    if remain < 0:
                        i = j % l
                        if i < start:
                            return -1
                        break
                if j == start + l - 1:
                    return start
            i += 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(sol.canCompleteCircuit(gas, cost))
