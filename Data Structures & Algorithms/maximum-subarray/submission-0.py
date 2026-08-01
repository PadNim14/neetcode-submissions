class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # currSum = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         for k in range(i, j):
        #             currSum += cubic complexity



        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
