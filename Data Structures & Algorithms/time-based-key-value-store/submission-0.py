class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        val = self.data.get(key, [])
        l, r = 0, len(val)-1
        while(l<=r):
            mid = (l+r) // 2
            if val[mid][0] <= timestamp:
                res = val[mid][1]
                l = mid+1
            else:
                r = mid - 1
        return res

