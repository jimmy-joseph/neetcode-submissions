class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                b1 = r // 3
                b2 = c // 3
                
                if val in rows[r] or val in columns[c] or val in boxes[(b1, b2)]:
                    return False

                rows[r].add(val)
                columns[c].add(val)
                boxes[(b1, b2)].add(val)

        return True