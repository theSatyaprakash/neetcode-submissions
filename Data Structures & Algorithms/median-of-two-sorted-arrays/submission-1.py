class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=0
        b=0
        l=[]
        while a<len(nums1) and b<len(nums2):
            if nums1[a]>nums2[b]:
                l.append(nums2[b])
                b+=1
            else:
                l.append(nums1[a])
                a+=1
        while a<len(nums1):
            l.append(nums1[a])
            a+=1
        while b<len(nums2):
            l.append(nums2[b])
            b+=1
        x=l[0]
        y=l[-1]
        m1=len(l)//2
        if len(l)%2==0:
            return (float((l[m1]+l[m1-1])/2))
        else:
            return (l[m1])

        


        