class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif len(stack) == 0 or stack.pop() != matches[char]:
                return False
        return len(stack) == 0 