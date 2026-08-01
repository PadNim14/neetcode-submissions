class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        second_arr = nums[:-1]
        first_arr = nums[1:]

        first_res = 0
        second_res = 0

        for n in first_arr:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        first_res = rob2

        rob1, rob2 = 0, 0
        
        for n in second_arr:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        second_res = rob2

        return max(nums[0], first_res, second_res)

