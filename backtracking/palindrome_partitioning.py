class Solution:
    def __init__(self):
        self.solution = []
        self.s = ""

    def partition(self, s: str) -> List[List[str]]:
        self.solution = []
        self.s = s
        self.backtrack([], "", 0)
        return self.solution

    def backtrack(self, stack, candidate, index):
        if index == len(self.s) and len(candidate) == 0:
            self.solution.append(stack.copy())
            return
        if index >= len(self.s):
            return
        candidate += self.s[index]
        if is_palindrome(candidate):
            kopy = stack.copy()
            kopy.append(candidate)
            self.backtrack(kopy, "", index+1)
        self.backtrack(stack.copy(), candidate, index+1)


def is_palindrome(string):
    return string == string[::-1]

