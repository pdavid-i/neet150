class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        top_k = [[] for _ in range(len(nums))]
        to_return = []
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for key in hashmap.keys():
            top_k[hashmap[key]-1].append(key)

        left=k
        print(top_k)
        for i in range(len(nums)-1, -1, -1):
            print(top_k[i])
            if(top_k[i] == []):
                continue
            to_return.extend(top_k[i])
            left-=len(top_k[i])
            if left <= 0:
                return to_return
        return to_return