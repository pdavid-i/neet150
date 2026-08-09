class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]]+=1
            else:
                a[s[i]]=1
            if t[i] in a:
                a[t[i]]-=1
            else:
                a[t[i]]=-1
        for x in a.values():
            if x != 0:
                return False
        return True 
            
            