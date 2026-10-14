class Solution:
    def __init__(self):
        self.solution = []

    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        self.trick = {}
        self.smarta(target, sorted(nums), [])
        return self.solution

    def smarta(self, left, to_pick, candidate):
        if left == 0:
            self.solution.append(candidate)
        for i,x in enumerate(to_pick):
            if i > 0 and to_pick[i] == to_pick[i-1]:
                continue
            elif left - x >= 0: 
                cnd = candidate.copy()
                cnd.append(x)
                self.smarta(left-x, to_pick[i+1:], cnd)