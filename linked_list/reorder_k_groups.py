class Solution:
    def reverseK(self, head, k):
        i = 1
        keith = head
        while i < k:
            if keith == None:
                return head
            keith = keith.next
            i += 1
        if keith == None:
            return head
        keith_next = keith.next
        prev = head
        current = head.next
        while current != keith:
            nextup = current.next
            current.next = prev
            prev = current
            current = nextup
        keith.next = prev
        head.next = self.reverseK(keith_next, k)
        return keith

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head
        return self.reverseK(head, k)
