"""
此题祥见207,就是要找出拓扑排序那个队列,所以不要倒着找,倒着找要多一步逆转数组
"""
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        next_courses = defaultdict(list)
        in_degree = [0] * numCourses
        ordered_courses = []
        for prerequisite in prerequisites:
            next_courses[prerequisite[1]].append(prerequisite[0])
            in_degree[prerequisite[0]] += 1
        for course in range(numCourses):
            if in_degree[course] == 0:
                ordered_courses.append(course)
        for course in ordered_courses:
            for next_course in next_courses[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    ordered_courses.append(next_course)
        return ordered_courses if len(ordered_courses) == numCourses else []


if __name__ == "__main__":
    sol = Solution()
    num = 2
    courses = [[1,0]]
    print(sol.findOrder(num, courses))