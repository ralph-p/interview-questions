class NumMatrix(object):
    
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dp = [[0 for r in range(len(matrix[0])+1)] for c in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r][c+1] = self.dp[r][c] + matrix[r][c]
        print(self.dp)
        

    def sumRegion(self, row1, col1, row2, col2):
        total = 0
        for x in range(row1,row2+1):
            total += self.dp[x][col2+1] - self.dp[x][col1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7]
]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(1, 2, 2, 4)
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
print(param_1)