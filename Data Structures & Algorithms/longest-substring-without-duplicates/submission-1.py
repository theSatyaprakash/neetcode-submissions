class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        seen=set()
        c=0
        m=0
        while j<len(s):
            if s[j] in seen:
                seen.remove(s[i])
                i+=1
               # c-=1
            else:
                seen.add(s[j])
                j+=1
               # c+=1
            m=max(j-i,m)
        return m
            
        