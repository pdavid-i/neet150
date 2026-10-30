class Solution:
    def numDecodings(self, s: str) -> int:
        current = s.replace("10", ".").replace("20", ".")
        if current.count('0') > 0:
            return 0
        twoset = set(['1', '2', '3', '4', '5', '6'])
        countit = 0
        found = {}

        def count_it(s):
            if not s:
                return 1
            if s in found:
                print(f'Cache hit for {s}')
                return found[s]
            if len(s) == 1:
                # any digit can be interpreted in one and only one way, 0's have been delet
                return 1
            first = s[0]
            second = s[1]
            # the basic way, we interpret as solo digit
            count = count_it(s[1:])
            found[s[1:]] = count
            if (first == '1' and second != '.') or (first == '2' and second in twoset):
                # add the way we interpret as composite
                composite = count_it(s[2:])
                found[s[2:]] = composite
                count += composite
            return count

        return count_it(current)