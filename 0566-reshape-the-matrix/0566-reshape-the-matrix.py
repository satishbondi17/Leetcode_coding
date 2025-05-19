class Solution(object):
    def matrixReshape(self, mat, r, c):
        m=len(mat)
        n=len(mat[0])
        res = [[0] * c for _ in range(r)]
      
        x,y=0,0
        if m*n!=r*c:
            return mat
        for i in range(0,m):
            for j in range(0,n):
                res[x][y]=mat[i][j]
                y+=1
                if y==c:
                    y=0
                    x+=1
        return res

        

        