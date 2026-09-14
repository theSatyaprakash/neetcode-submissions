class Solution:
    def mergeTriplets(self, triplets, target):
        a = b = c = 0

        for x, y, z in triplets:
            # Ignore triplets that exceed target
            if x > target[0] or y > target[1] or z > target[2]:
                continue

            a = max(a, x)
            b = max(b, y)
            c = max(c, z)

        return [a, b, c] == target
        