"""
此题思路:
用一个栈逆向保存数组,数组起始元素在栈顶,末尾元素在栈底
巧妙利用每次next之前都需要用hasNext进行判断这一点,可以在hasNext中做点事情,如果栈顶的是一个数组,就把数组拿出来,
从尾到头逆向压进栈里,直到栈顶的是数字为止,在next调用时就可以直接从栈顶弹出一个数字来用
注意,因为名字迭代器的暗示,并不需要在__init__中就对整个嵌套数组完全展开,用的时候再去一层层剥开就行了
"""


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.queue = nestedList
        self.queue.reverse()

    def next(self):
        """
        :rtype: int
        """
        return self.queue.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.queue) > 0 and not self.queue[-1].isInteger():
            tmp = self.queue.pop().getList()[::-1]
            self.queue.extend(tmp)
        return len(self.queue) > 0


# Your NestedIterator object will be instantiated and called as such:
if __name__ == '__main__':
    i, v = NestedIterator([1, [2, 3], [4, [5, 6]]]), []
    while i.hasNext():
        v.append(i.next())
    print(v)
