class Solution:
    def isValidSudoku(self, l: List[List[str]]) -> bool:
        col=collections.defaultdict(set)
        row=collections.defaultdict(set)
        b=collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if l[r][c]==".":
                    continue
                if (l[r][c] in row[r] or
                     l[r][c] in col[c] or
                     l[r][c] in b[(r//3,c//3)] ):
                     return False
                row[r].add(l[r][c])
                col[c].add(l[r][c])
                b[(r//3,c//3)].add(l[r][c])
        return True



        