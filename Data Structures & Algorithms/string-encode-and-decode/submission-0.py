class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded="º"
        for st in strs:
            encoded+=st+'º'
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split("º")[1:-1]
