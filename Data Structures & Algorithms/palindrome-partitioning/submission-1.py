class Solution:
    def partition(self, s):
        result = []

        def is_palindrome(sub):
            l, r = 0, len(sub) - 1
            while l<r:
                if sub[l]==sub[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return result