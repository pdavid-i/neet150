class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        try:
            while slow != None and fast != None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
        except AttributeError:
            return False
