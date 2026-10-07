# Problem No.209
# https://leetcode.com/problems/reverse-linked-list


# Solution 1:


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp1 = head
        temp3 = None
        while temp1 is not None:
            temp2 = temp1.next
            temp1.next = temp3
            temp3 = temp1
            temp1 = temp2
        return temp3


# Solution 2:

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
