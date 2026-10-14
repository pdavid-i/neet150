class Solution:
    def __init__(self):
        self.d2l = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        self.solution = []

    def letterCombinations(self, digits: str) -> List[str]:
        self.solution = []
        if len(digits) != 0:
            self.backtrack("", 0, digits)
        return self.solution
    
    def backtrack(self, candidate, index, digits):
        if len(candidate) == len(digits):
            self.solution.append(candidate)
            return
        for letter in self.d2l[digits[index]]:
            self.backtrack(candidate+letter, index+1, digits)
