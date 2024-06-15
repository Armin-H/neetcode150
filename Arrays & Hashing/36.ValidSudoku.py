from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Neetcode's solution was almost identical
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        n = len(board)

        for i in range(n): 
            for j in range(n):  
                element = board[i][j]
                if element != '.':
                    if element in rows[i] or element in cols[j] or element in boxes[(i//3,j//3)]: 

                        return False
                    else: 
                        rows[i].add(element)
                        cols[j].add(element)
                        boxes[(i//3 , j//3)].add(element)
        return True