class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for x in nums:
            if x in a:
                return True
            a[x]=True
        return False