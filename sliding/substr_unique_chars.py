    def lengthOfLongestSubstring(self, s: str) -> int:
        left = current = longest = right = 0
        uniques = set()
        while right < len(s):
            if s[right] not in uniques:
                uniques.add(s[right])
                current += 1
                longest = max(current, longest)
            else:
                while s[right] in uniques:
                    uniques.remove(s[left])
                    current -= 1
                    left += 1
                uniques.add(s[right])
                current += 1
            right += 1
        return longest