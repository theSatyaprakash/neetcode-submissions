class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0
        s=[] #pair of index and height
        for i ,h in enumerate(heights):
            start=i
            while s and s[-1][1]>h:
                index,height=s.pop()
                maxarea=max(maxarea,height*(i-index))
                start=index
            s.append((start,h))
        for i,h in s:
            maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea     
        