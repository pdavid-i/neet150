import sys
sys.setrecursionlimit(3000)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        mleft = 0
        mright = 0
        computed = {}
        solution = set()

        def is_palindrome(left, right):
            if left < 0 or right >= len(s):
                return

            key = (left, right)

            if key in computed:
                return computed[key]

            if left >= right:
                result = True
            elif s[left] != s[right]:
                result = False
            else:
                result = is_palindrome(left + 1, right - 1)
            computed[key] = result
            return result

        def workit(left, right):
            if left < 0 or right >= len(s):
                return
            nonlocal mleft, mright
            if right - left > mright - mleft:
                mright = right
                mleft = left
                
            if is_palindrome(left-1, right+1):
                workit(left-1, right+1)
            elif is_palindrome(left, right+1):
                workit(left, right+1)

        for i in range(0, len(s)):
            workit(i, i)
        return s[mleft:mright+1]