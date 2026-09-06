class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def back(i,sub):
            if i==len(nums):
                res.append(sub[::])
                return
            #all sub that include i
            sub.append(nums[i])
            back(i+1,sub)
            sub.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            back(i+1,sub)
        back(0,[])
        return res

