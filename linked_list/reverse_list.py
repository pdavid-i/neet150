class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        past = None
        while current != None:
            nextone = current.next
            current.next = past
            past = current
            current = nextone
        return past
