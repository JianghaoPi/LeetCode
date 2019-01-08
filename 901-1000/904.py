class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        fast = 0
        slow = 0
        res = 0
        record = set()
        while fast < len(tree):
            record.add(tree[fast])
            if fast == len(tree) - 1 and len(record) <= 2:
                return max(res, fast - slow + 1)
            if len(record) > 2:
                fast -= 1
                res = max(fast-slow+1, res)
                slow = fast
                while slow > 0 and tree[slow-1] == tree[fast]:
                    slow -= 1
                record = {tree[slow]}
            fast += 1
        return res


sol = Solution()
print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))