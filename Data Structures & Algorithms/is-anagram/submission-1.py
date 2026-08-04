class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        for ltr in s:
            if ltr in a:
                a[ltr]+=1
            else:
                a[ltr]=1
        for ltr in t:
            if ltr in a and a[ltr] > 0:
                a[ltr]-=1
            else:
                return False
        return len(s) == len(t)