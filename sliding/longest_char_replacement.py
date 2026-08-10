class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        left = current = longest = right = 0
        most_def = s[0]
        freq = {}
        while right < len(s):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            current += 1
            if max(freq.values()) + k >= right - left + 1:
                longest = max(longest, current)
            else:
                freq[s[left]] -= 1
                current -= 1
                left += 1
            right += 1

        return longest
        longest = max(current + min(k - misses, len(s) - current), longest)
        return longest