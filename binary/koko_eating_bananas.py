class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        current = right = big_pile = max(piles)
        left = 1

        while (left < right):
            mid = left + (right - left) // 2
            validate_mid = self.validate_speed(piles, mid, h)
            if mid - 1 != 0:
                validate_lower = self.validate_speed(piles, mid-1, h)
            else:
                validate_lower = False
            if (validate_mid):
                right = mid 
                current = min(current, mid)
            else:
                if validate_lower:
                    return mid-1
                left = mid + 1
        return current

    def validate_speed(self, piles, speed, h) -> bool:
        for pile in piles:
            hours = -(-pile // speed) 
            h -= hours
            if h < 0:
                return False
        return True