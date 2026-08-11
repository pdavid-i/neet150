class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)
        og = [0] * 26
        current = [0] * 26
        for i in range(len(s1)):
            og[tonr(s1[i])] += 1
            current[tonr(s2[i])] += 1
        if og == current:
            return True
        while right < len(s2):
            current[tonr(s2[left])] -= 1
            current[tonr(s2[right])] += 1
            if og == current:
                return True
            left += 1
            right += 1
        return False


def tonr(letter: str) -> int:
    return ord(letter) - ord("a")