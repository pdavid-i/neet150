import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        maxes = []
        for i in range(k):
            heapq.heappush_max(heap, [nums[i], i])
        maxes.append(heap[0][0])
        for i in range(k, len(nums), 1):
            heapq.heappush_max(heap, [nums[i],i])
            max_index = heap[0][1]
            while not (i - k < heap[0][1]):
                heapq.heappop_max(heap)
            maxes.append(heap[0][0])
        return maxes
