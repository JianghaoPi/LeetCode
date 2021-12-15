package problem0002

// Definition for singly-linked list.
type ListNode struct {
	Val int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	res := &ListNode{Val: l1.Val+l2.Val}
	cur := res
	for  {
		if l1 != nil || l2 != nil {
			if l1 != nil {
				l1 = l1.Next
			}
			if l2 != nil {
				l2 = l2.Next
			}
		}
		if l1 == nil && l2 == nil {
			break
		}
		value1 := 0
		if l1 != nil {
			value1 = l1.Val
		}
		value2 := 0
		if l2 != nil {
			value2 = l2.Val
		}
		cur.Next = &ListNode{Val: value1+value2}
		cur = cur.Next
	}
	cur = res
	for  {
		if cur.Val > 9 {
			if cur.Next == nil {
				cur.Next = &ListNode{}
			}
			cur.Next.Val += cur.Val / 10
			cur.Val = cur.Val % 10
		}
		cur = cur.Next
		if cur == nil {
			return res
		}
	}
}