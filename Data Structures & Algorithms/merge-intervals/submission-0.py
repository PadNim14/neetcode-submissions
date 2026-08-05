class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        startVal, endVal = intervals[0]

        for interval in intervals[1:]:
            curStart, curEnd = interval
            lastEndVal = res[-1][1]
            if curStart <= lastEndVal:
                res[-1][1] = max(curEnd, lastEndVal)
            else:
                res.append(interval)
        

        return res


        