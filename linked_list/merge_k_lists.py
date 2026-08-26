import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mindex = -1
        prev = None
        merged = None
        qq = []
        for index, lis in enumerate(lists):
            if lis != None:
                heapq.heappush(qq, (lis.val, index))
        while len(qq) > 0:
            node_val, index = heapq.heappop(qq)
            current = ListNode(node_val)
            if prev != None:
                prev.next = current
            else:
                merged = current
            prev = current
            lists[index] = lists[index].next
            if lists[index] != None:
                heapq.heappush(qq, (lists[index].val, index))
        return merged
