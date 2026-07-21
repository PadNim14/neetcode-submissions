class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # naive solution
        # time O(n^2) space O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


        # optimal solution with dictionary

        # diffDict = {}
        # res = []

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in diffDict:
        #         return [diffDict[diff], i]
        #     diffDict[num] = i