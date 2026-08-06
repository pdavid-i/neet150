class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dic = {}
        longest = 1
        for i, v in enumerate(nums):
            dic[v]=True
        for i, v in enumerate(nums):
            current = 1
            if v-1 in dic:
                continue
            next_number = v+1
            while next_number in dic:
                current+=1
                next_number+=1
            if current > longest:
                longest = current
        return longest 