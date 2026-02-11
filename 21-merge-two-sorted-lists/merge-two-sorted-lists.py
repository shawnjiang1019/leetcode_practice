# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        result_p = result
        temp = result
        p1 = list1
        p2 = list2
        while p1 or p2:
            if p1 and p2:
                if p1.val <= p2.val:
                    result_p.next = ListNode(p1.val)
                    result_p = result_p.next
                    p1 = p1.next
                else:
                    result_p.next = ListNode(p2.val)
                    result_p = result_p.next
                    p2 = p2.next
            elif not p1:
                result_p.next = ListNode(p2.val)
                result_p = result_p.next
                p2 = p2.next
            elif not p2:
                result_p.next = ListNode(p1.val)
                result_p = result_p.next
                p1 = p1.next
        return result.next
        