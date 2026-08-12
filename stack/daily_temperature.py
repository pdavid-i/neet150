    class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        solution = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]:
                before_index = stack.pop()[1]
                solution[before_index] = index - before_index
            stack.append([value, index])
        return solution