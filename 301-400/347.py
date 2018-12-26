class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        record_dict = {}
        for i in nums:
            if i in record_dict:
                record_dict[i] += 1
            else:
                record_dict[i] = 1
        freq = list(record_dict.items())
        self.quickSort(freq, 0, len(freq)-1)
        res = [t[0] for t in freq[:k]]
        return res

    def quickSort(self, freq_list, left, right):
        if left >= right:
            return
        i = left
        j = right
        pivot = freq_list[left]
        while i < j:
            while i < j and freq_list[j][-1] <= pivot[-1]:
                j -= 1
            if j > i:
                freq_list[i] = freq_list[j]
            while i < j and freq_list[i][-1] >= pivot[-1]:
                i += 1
            if i < j:
                freq_list[j] = freq_list[i]
        freq_list[i] = pivot
        self.quickSort(freq_list, left, i-1)
        self.quickSort(freq_list, i+1, right)

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,2], 2))