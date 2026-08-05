class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        top_k = [[] for _ in range(len(nums))]
        to_return = []
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for key in hashmap.keys():
            top_k[hashmap[key]-1].append(key)

        top_k.reverse()
        left=k
        print(top_k)
        offset = 0
        for i in range(k):
            while (top_k[i+offset] == []):
                offset+=1
            to_return.extend(top_k[i+offset])
            left-=len(top_k[i+offset])
            if left <= 0:
                return to_return
        return to_return

