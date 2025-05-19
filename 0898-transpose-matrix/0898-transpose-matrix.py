class Solution(object):
    def transpose(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        res = [[0] * m for _ in range(n)] 
        
        for i in range(0,m):
            for j in range(0,n):
                res[j][i]=matrix[i][j]
        return res

        