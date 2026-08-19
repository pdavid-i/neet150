class TimeMap:
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timemap.get(key) == None:
            self.timemap[key] = [[value, timestamp]]
        else:
            self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.timemap.get(key) == None:
            return ""
        # If the timestamp asked is bigger than last elem, return it
        if self.timemap[key][-1][1] <= timestamp:
            return self.timemap[key][-1][0]
        # Binary search value based
        left = 0
        right = len(self.timemap[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            if (
                self.timemap[key][mid][1] <= timestamp
                and self.timemap[key][mid + 1][1] > timestamp
            ):
                return self.timemap[key][mid][0]
            elif self.timemap[key][mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return ""
