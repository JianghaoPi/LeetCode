"""
经典解法：要向右移动k个位置，比如[1,2,3,4,5,6,7]移动3个位置到[5,6,7,1,2,3,4]
可以看成先把前n-k位[1,2,3,4]中心对称，后k位中心对称，然后整体中心对称
"""
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        self.symmetry(nums, 0, length-k-1)
        self.symmetry(nums, length-k, length-1)
        self.symmetry(nums, 0, length-1)

    def symmetry(self, nums, start, stop):
        left = start
        right = stop
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    sol = Solution()
    num = [1,2,3,4,5,6,7]
    sol.rotate(num, 3)
    print(num)
