class Solution:
    def __init__(self):
        self.ans = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.workit([], nums)
        return self.ans

    def workit(self, candidate, left):
        if len(left) == 0:
            self.ans.append(candidate)
        for i in range(len(left)):
            new_candidate = candidate.copy()
            new_candidate.append(left[i])
            new_left = left.copy()
            new_left.pop(i)
            self.workit(new_candidate, new_left)