class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # result
        res = []
        startNew, endNew = newInterval
        for idx, interval in enumerate(intervals):
            currStart, currEnd = interval
            if endNew < currStart:
                return res + [[startNew, endNew]] + intervals[idx:]
            elif currEnd < startNew:
                res.append([currStart, currEnd])
            else:
                startNew = min(startNew, currStart)
                endNew =  max(endNew, currEnd)
        res.append([startNew, endNew])
        return res
        
        
