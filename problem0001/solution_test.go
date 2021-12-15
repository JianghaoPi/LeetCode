package problem0001

import (
	"testing"
)

func TestTwoSum(t *testing.T)  {
	nums1 := []int{3, 2, 4}
	target := 6
	ans := twoSum(nums1, target)
	t.Error(ans)
}
