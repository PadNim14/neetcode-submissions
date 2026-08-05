class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        startVal, endVal = intervals[0]
        count = 0
        for interval in intervals[1:]:
            curStart, curEnd = interval
            if curStart >= endVal:
                endVal = curEnd
            else:
                count += 1
                endVal = min(endVal, curEnd)
        return count
