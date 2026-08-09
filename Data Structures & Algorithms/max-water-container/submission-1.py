class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        m=-100000
        while i<j:
            s=min(heights[i], heights[j])
            m=max(m,(j-i)*s)
            if heights[i] <heights[j]:
                i+=1
            else :
                j-=1
        return m


        