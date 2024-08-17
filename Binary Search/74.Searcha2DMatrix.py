class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """my solution"""
        def get_matrix_coords(idx,n):
            row_idx = idx // n 
            col_idx = idx % n
            return row_idx, col_idx 


        m = len(matrix)
        n = len(matrix[0])

        l,r= 0, m*n - 1

        while l <= r: 
            middle_idx = (l + r) // 2
            row_idx, col_idx = get_matrix_coords(middle_idx,n) 
            middle = matrix[row_idx][col_idx]
            if middle == target: 
                return True
            elif middle > target: 
                r = middle_idx - 1
            elif middle < target: 
                l = middle_idx + 1

        return False
    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """neetcode's solution. he is using two binary searches. My solution is more elegant than his"""
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
