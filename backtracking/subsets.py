class Solution:
    def __init__(self):
        self.ans = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.dabos(nums, [])
        return self.ans

    def dabos(self, left, solution):
        print(f"Called, left:{left}, solution:{solution}")
        if len(left) == 0:
            print(f"Found {solution}")
            self.ans.append(solution.copy())
        else:
            self.dabos(left[1:].copy(), solution.copy())
            solution.append(left[0])
            self.dabos(left[1:].copy(), solution.copy())