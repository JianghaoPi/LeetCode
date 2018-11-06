"""
此题实际上是一个拓扑排序,要确定一个有向图中是否存在着环.
首先用一个数组next_nodes存放每门课直接后续课程,然后用一个数组in_degree存放每个节点的入度,用一个队列存放入度为0的点.
只需要循环操作,找出入度为0的点,从有向图中拆出来放入队列,将相应的直接后续课程入度减1,看看其是否入度为0,是就放入队列
如果最后所有课程都能放入这个队列,那么这个队列的出队顺序就是一个拓扑排序,按这个顺序去选课就不会有问题.

此题还有一种类似解法就是反向操作,先找出没有后置课程的课,再不停找出度为0的课程

在做这题的过程中,对python加深了3个理解
1.初始化一个二维数组不能用[[]]*n的方式,这样其中的每一个矩阵实际上引用的是同一个地址,变一个就是所有都变
2.队列的使用不一定非要用queue,合理利用内置的列表一样可以达到这个效果
3.defaultdict可以传入默认工厂函数,然后在使用的时候就再也不用判断这个键是否存在于字典中,直接取值赋值就行,不会有keyError
"""
from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        next_nodes = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        free_courses = []
        for edge in prerequisites:
            next_nodes[edge[1]].append(edge[0])
            in_degree[edge[0]] += 1
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                free_courses.append(i)
        for i in free_courses:
            for j in next_nodes[i]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    free_courses.append(j)
        return len(free_courses) == numCourses

    def canFinish1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prev_courses = defaultdict(list)
        out_degree = [0] * numCourses
        free_courses = []
        for edge in prerequisites:
            prev_courses[edge[0]].append(edge[1])
            out_degree[edge[1]] += 1
        for course in range(numCourses):
            if out_degree[course] == 0:
                free_courses.append(course)
        for course in free_courses:
            for prev_course in prev_courses[course]:
                out_degree[prev_course] -= 1
                if out_degree[prev_course] == 0:
                    free_courses.append(prev_course)
        return len(free_courses) == numCourses

if __name__ == '__main__':
    sol = Solution()
    numCourses = 2
    courses = [[1,0]]
    print(sol.canFinish(numCourses, courses))