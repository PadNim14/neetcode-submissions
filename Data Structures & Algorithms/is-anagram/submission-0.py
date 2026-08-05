class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 1
            if t[i] not in tMap:
                tMap[t[i]] = 1
            if s[i] in sMap:
                sMap[s[i]] += 1
            if t[i] in tMap:
                tMap[t[i]] += 1
               
        return sMap == tMap
