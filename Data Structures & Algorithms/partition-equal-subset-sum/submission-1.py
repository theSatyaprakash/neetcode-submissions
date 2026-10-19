class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        # Odd total cannot be divided equally
        if total % 2 != 0:
            return False

        target = total // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            nxtdp=set()
            for t in dp:
                nxtdp.add(nums[i]+t)
                nxtdp.add(t)
            dp=nxtdp
        return True if target in dp else False