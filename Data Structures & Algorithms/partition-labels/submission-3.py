class Solution:
    def partitionLabels(self, s):
        # Store last occurrence of every character
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        ans = []

        size = 0
        end = 0

        for i in range(len(s)):
            # Extend partition to last occurrence
            # of current character
            size+=1
            end = max(end, last[s[i]])

            # Partition is complete
            if i == end:
                ans.append(size)
                size = 0

        return ans