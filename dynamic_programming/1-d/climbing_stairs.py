class Solution:
    def __init__(self):
        self.dic = {}

    def climbStairs(self, n: int) -> int:
        return self.count(n)

    def count(self, left):
        if left < 0:
            return 0
        if left == 0:
            return 1

        return self.get_or_compute(left-1) + self.get_or_compute(left-2)

    def get_or_compute(self, value):
        if value in self.dic:
            return self.dic[value]
        else:
            computed = self.count(value)
            self.dic[value] = computed
            return computed