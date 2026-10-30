class Solution:
    def rob(self, nums: List[int]) -> int:
        steal_until = {}
        if len(nums) == 1:
            return nums[0]

        def sneaky(i, steal):
            if i >= len(nums):
                return
            steal += nums[i]
            if i in steal_until:
                if steal_until[i] >= steal:
                    return
                steal_until[i] = steal
            else: 
                steal_until[i] = steal
            sneaky(i+2, steal)
            sneaky(i+3, steal)

        sneaky(0, 0)
        sneaky(1, 0)
        print(steal_until)
        return max(steal_until[len(nums)-1], steal_until[len(nums)-2])