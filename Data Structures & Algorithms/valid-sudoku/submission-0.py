class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        columns = defaultdict(list)
        boxes = defaultdict(list)

        for index, row in enumerate(board):
            for entry_index, entry in enumerate(row):
                if entry.isnumeric():
                    rows[index].append(entry)
                    columns[entry_index].append(entry)
                    box_index1 = index // 3
                    box_index2 = entry_index // 3
                    boxes[(box_index1, box_index2)].append(entry)
        
        for row in rows.values():
            if len(set(row)) != len(row):
                return False
            
        for column in columns.values():
            if len(set(column)) != len(column):
                            return False
        for box in boxes.values():
            if len(set(box)) != len(box):
                            return False

        return True