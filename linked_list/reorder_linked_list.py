class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        length = 0
        reverse = ListNode()
        past = ListNode(-1)
        while current != None:
            length += 1
            current = current.next
        if length == 1:
            return
        second_len = length // 2
        first_len = length - second_len

        current = head
        past = None
        for i in range(1, length + 2, 1):
            nextup = current.next

            if i == first_len:
                first_end = current
            if i > first_len:
                reverse = current
                reverse.next = past
                past = current
                current = nextup
            if current == None:
                break
            current = nextup

        first_end.next = None
        current = head
        for i in range(1, second_len + 1, 1):
            aux = reverse
            nextup = current.next
            current.next = aux
            if reverse != None:
                reverse = reverse.next
                aux.next = nextup
                current = nextup

        return
