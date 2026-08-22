# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged = ListNode()
        current = merged
        past = None
        while list1 != None or list2 != None:
            if list1 == None:
                current.next = list2
                print("l1 noine")
                break
            if list2 == None:
                current.next = list1
                print("l2 noine")
                break

            aux = ListNode()
            current.next = aux
            if list1.val < list2.val:
                aux.val = list1.val
                list1 = list1.next
            else:
                aux.val = list2.val
                list2 = list2.next
            current = current.next
        return merged.next
