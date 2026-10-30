class Solution:
    def rob(self, nums: List[int]) -> int:
        steal_until = {}
        if len(nums) == 1:
            return nums[0]

        def sneaky(i, steal, start_first):
            if i >= len(nums) - start_first:
                return
            steal += nums[i]
            if i in steal_until:
                if steal_until[i] >= steal:
                    return
                steal_until[i] = steal
            else: 
                steal_until[i] = steal
            sneaky(i+2, steal, start_first)
            sneaky(i+3, steal, start_first)

        sneaky(0, 0, 1)
        sneaky(1, 0, 0)
        nums.reverse()
        sneaky(0, 0, 1)
        print(steal_until)
        return max(steal_until.values())