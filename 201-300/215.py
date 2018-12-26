class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.mergeSort(nums, 0, len(nums)-1)
        return nums[-k]

    def mergeSort(self, nums, left, right):
        if left == right:
            return
        mid = (right + left) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid+1, right)
        result = []
        i = left
        j = mid+1
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                result.append(nums[i])
                i += 1
            else:
                result.append(nums[j])
                j += 1
        if i <= mid:
            result.extend(nums[i:mid+1])
        if j <= right:
            result.extend(nums[j:right+1])
        nums[left:right+1] = result

    def quickSort(self, nums, left, right):
        if left >= right:
            return
        i = left
        j = right
        pivot = nums[left]
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[j] = nums[i]
        nums[i] = pivot
        self.quickSort(nums, left, i-1)
        self.quickSort(nums, i+1, right)

if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
    nums = [3,2,3,1,2,4,5,5,6]
    sol.quickSort(nums, 0, len(nums)-1)
    print(nums)