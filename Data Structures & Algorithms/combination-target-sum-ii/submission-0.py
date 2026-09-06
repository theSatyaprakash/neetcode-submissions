class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(i,cur,target):
            if target==0:
                res.append(cur.copy())
            if target<=0:
                return
            pre=-1
            for j in range(i,len(nums)):
                if pre==nums[j]:
                    continue
                cur.append(nums[j])
                dfs(j+1,cur,target-nums[j])
                cur.pop()
                pre=nums[j]
                
        dfs(0,[],target)
        return res
