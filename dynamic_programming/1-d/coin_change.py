class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = {}

        def workit(count, left):
            if left < 0:
                return
            current = amount - left
            if current in memo and memo[current] <= count:
                return
            memo[current] = count
            for x in coins:
                workit(count+1, left-x)

        workit(0, amount)
        return memo.get(amount, -1)
