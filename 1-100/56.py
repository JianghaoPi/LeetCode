"""
思路：先根据左端点排序，然后遍历合并排序nlogn，遍历n，故为O(nlogn)
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        self.quickSort(intervals, 0, len(intervals)-1)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start <= result[-1].end:
                if intervals[i].end > result[-1].end:
                    result[-1].end = intervals[i].end
            else:
                result.append(intervals[i])
        return result

    def quickSort(self, intervals, left, right):
        if left >= right:
            return
        i = left
        j = right
        pivot = intervals[left]
        while i < j:
            while i < j and intervals[j].start >= pivot.start:
                j -= 1
            if i < j:
                intervals[i] = intervals[j]
            while i < j and intervals[i].start <= pivot.start:
                i += 1
            if i < j:
                intervals[j] = intervals[i]
        intervals[i] = pivot
        self.quickSort(intervals, left, i-1)
        self.quickSort(intervals, i+1, right)
