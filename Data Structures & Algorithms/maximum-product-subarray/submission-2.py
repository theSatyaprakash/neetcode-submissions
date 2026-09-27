class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        answer = nums[0]

        for x in nums[1:]:

            if x < 0:
                maxProd, minProd = minProd, maxProd

            maxProd = max(x, maxProd * x)
            minProd = min(x, minProd * x)

            answer = max(answer, maxProd)

        return answer