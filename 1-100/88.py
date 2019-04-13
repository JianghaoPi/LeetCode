"""
从后往前排
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
        i = m-1
        j = n-1
        for k in range(m+n-1, -1, -1):
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            if i < 0:
                for x in range(j+1):
                    nums1[x] = nums2[x]
                return
            if j < 0:
                return
