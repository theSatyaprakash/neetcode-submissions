class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for i in strs:
            k="".join(sorted(i))
            if k not in l:
                l[k]=[]
            l[k].append(i)
        return list(l.values())
