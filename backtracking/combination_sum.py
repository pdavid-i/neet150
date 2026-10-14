class Solution:
    def __init__(self):
        self.solution = []

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.solution = []
        self.smarta(target, nums, [])
        return self.solution

    def smarta(self, left, to_pick, candidate):
        if left == 0 and candidate:
            self.solution.append(candidate.copy())
        for i,x in enumerate(to_pick):
            if left - x >= 0: 
                cnd = candidate.copy()
                cnd.append(x)
                self.smarta(left-x, to_pick[i:], cnd)