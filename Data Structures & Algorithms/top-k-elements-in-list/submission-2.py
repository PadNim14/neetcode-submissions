class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hMap = {}
        res = []

        for num in nums:
            print(num)
            if num in hMap:
                hMap[num] += 1
            else:
                hMap[num] = 1

        sortedFreq = dict(sorted(hMap.items(), key=lambda item: item[1], reverse=True))
        for val in sortedFreq:
            res.append(val)
            if len(res) == k:
                return res
    
        