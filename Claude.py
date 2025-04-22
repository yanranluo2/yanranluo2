class Solution:
    def maximumValueSum(self, board):
        m, n = len(board), len(board[0])
        memo = {}
        
        def backtrack(rook_count, used_rows, used_cols, current_sum):
            # Base case: we've placed all 3 rooks
            if rook_count == 3:
                return current_sum
            
            # Check if we've already computed this state
            key = (rook_count, used_rows, used_cols)
            if key in memo:
                return memo[key]
            
            max_sum = float('-inf')
            
            # Try placing a rook in every available cell
            for row in range(m):
                if (used_rows >> row) & 1:  # Skip if row is already used
                    continue
                    
                for col in range(n):
                    if (used_cols >> col) & 1:  # Skip if column is already used
                        continue
                    
                    # Place a rook at this position and update used rows/columns
                    new_used_rows = used_rows | (1 << row)
                    new_used_cols = used_cols | (1 << col)
                    
                    # Recursive call to place remaining rooks
                    max_sum = max(max_sum, backtrack(
                        rook_count + 1, 
                        new_used_rows, 
                        new_used_cols, 
                        current_sum + board[row][col]
                    ))
            
            # Memoize the result for this state
            memo[key] = max_sum
            return max_sum
        
        return backtrack(0, 0, 0, 0)