class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        m=1
        c=1
        for i in range(len(nums)-1):
            if (nums[i+1]==nums[i]+1 ):
                c+=1
            elif nums[i+1]==nums[i]:
                continue
            else:
                m=max(m,c)
                c=1
        return max(m,c)
        