class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while (left <= right):
            while s[left].isalnum() == False: 
                left += 1
                if left == len(s):
                    return True
            while not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                print(s[left])
                print(s[right])
                return False
            left += 1
            right -= 1
        return True