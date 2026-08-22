class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        dic = {}
        prev = None
        new_head = old_head = head
        while head != None:
            current = Node(head.val)
            if prev == None:
                new_head = current
            else:
                prev.next = current
            prev = current
            dic[head] = current
            head = head.next

        current = new_head
        while old_head != None:
            try:
                current.random = dic[old_head.random]
            except:
                current.random = None
            current = current.next
            old_head = old_head.next
        return new_head
