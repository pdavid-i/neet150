class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for st in strs: 
            le_key = tuple(self.customHash(st))
            if le_key in groups:
                groups[le_key].append(st)
            else:
                groups[le_key] = [st]
        return(list(groups.values()))

    def customHash(self, to_hash: str) -> List[int]:
        letter_hash = [0] * 26
        for letter in to_hash:
            letter_hash[ord(letter)-ord('a')]+=1
        return letter_hash