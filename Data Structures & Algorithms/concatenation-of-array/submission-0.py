class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        orgLen = len(nums)
        newLen = 2 * orgLen
        output = [0] * newLen

        for i in range(orgLen):
            output[i] = output[i + orgLen] = nums[i]
        return output

        