package problem0002

func lengthOfLongestSubstring(s string) int {
	lastIndexRecord := make(map[uint8]int)
	startIndex := -1
	maxLength := 0
	for i := 0; i < len(s); i++ {
		index, ok := lastIndexRecord[s[i]]
		if ok {
			if index > startIndex {
				startIndex = index
			}
		}
		length := i - startIndex
		if length > maxLength {
			maxLength = length
		}
		lastIndexRecord[s[i]] = i
	}
	return maxLength
}