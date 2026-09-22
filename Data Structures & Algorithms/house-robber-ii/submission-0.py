class Solution:
    def rob(self, nums):
        
        def rob_linear(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        if len(nums) == 1:
            return nums[0]

        case1 = rob_linear(nums[:-1])  # Don't rob last
        case2 = rob_linear(nums[1:])   # Don't rob first

        return max(case1, case2)