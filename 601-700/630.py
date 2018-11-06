"""
贪心法,先根据DDL排个序,然后根据DDL从前往后,尽量找时间短的课程上

本题用了一个大顶堆(heapq只能实现小顶堆,所以传入相反数,取得相同效果)
遍历排好序的课程,先把课程入堆,更新选上这门课后的结束时间,然后判断结束时间是否大于新加进去的课程的DDL,
如果大于,就去掉堆顶(时间最长)的课程,同时更新总的结束时间.
"""

import heapq
class Solution:
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        sorted_by_end = sorted(courses, key=lambda x: x[-1])
        end = 0
        heap = []
        for course in sorted_by_end:
            heapq.heappush(heap, -course[0])
            end += course[0]
            if end > course[1]:
                end += heapq.heappop(heap)
        return len(heap)


if __name__ == '__main__':
    sol = Solution()
    courses = [[5,5],[4,6],[2,6]]
    print(sol.scheduleCourse(courses))