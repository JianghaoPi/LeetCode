package problem0001

func twoSum(nums []int, target int) []int {
	recordMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		complement := target - nums[i]
		if index, ok := recordMap[complement]; ok {
			return []int{i, index}
		}
		recordMap[nums[i]] = i
	}
	return nil
}
