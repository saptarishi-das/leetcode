from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry

            current.next = ListNode(s % 10)
            carry = int (s / 10)

            l1 = l1.next
            l2 = l2.next
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


l1 = ListNode(1, ListNode(8, ListNode(3)))
l2 = ListNode(4, ListNode(5, ListNode(9)))

result = Solution().addTwoNumbers(l1, l2)
print(result)