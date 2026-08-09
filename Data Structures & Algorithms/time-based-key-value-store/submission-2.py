class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # O(n) linear solution
        # if key not in self.timeMap:
        #     return ""
        # seen = -1
        # print(self.timeMap[key])
        # for time in self.timeMap[key]:
        #     if time <= timestamp:
        #         seen = max(seen, time)
        # return "" if seen == -1 else self.timeMap[key][seen][-1]        
        # O(log n) using binary search

        res, values = "", self.timeMap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
