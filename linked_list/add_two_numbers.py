class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carryover = 0
        prev = None
        c1 = l1
        c2 = l2
        while c1 != None and c2 != None:
            # compute the digit sum, create new node
            summ = c1.val + c2.val + carryover

            # create the new digit node and link it
            new_node = ListNode(summ % 10)
            carryover = summ // 10
            if prev != None:
                prev.next = new_node
            else:
                summit = new_node

            # increment
            prev = new_node
            c1 = c1.next
            c2 = c2.next

        if c2 != None:
            self.looseEnd(c2, prev, carryover)
        elif c1 != None:
            self.looseEnd(c1, prev, carryover)
        elif carryover != 0:
            new_node = ListNode(1)
            prev.next = new_node

        return summit

    def looseEnd(self, node, prev, carryover):
        summ = node.val + carryover
        node.val = summ % 10
        carryover = summ // 10
        prev.next = node
        if carryover == 1:
            if node.next != None:
                return self.carryover(node.next)
            node.next = ListNode(1)

    def carryover(self, head):
        if head.val != 9:
            head.val += 1
            return

        head.val = 0
        if head.next == None:
            new_node = ListNode(1)
            head.next = new_node
        else:
            self.carryover(head.next)
