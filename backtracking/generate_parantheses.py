class Solution:
    def __init__(self):
        self.sol = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.sol = []
        self.backtrack("", 0, n)
        return self.sol

    def backtrack(self, candidate, score, n):
        if len(candidate) > 2*n or score < 0:
            return
        if len(candidate) == 2*n and score == 0:
            self.sol.append(candidate)
        candidate+="("
        self.backtrack(candidate, score+1, n)
        candidate = candidate[:-1] + ")"
        self.backtrack(candidate, score-1, n)