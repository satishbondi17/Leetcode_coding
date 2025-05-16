class Solution(object):
    def diagonalSum(self, mat):
        n=len(mat)
        sum=0
        for i in range(0,n):
            sum+=mat[i][i]
            sum+=mat[i][n-1-i]
        if n%2==1:
            sum-=mat[n//2][n//2]
        return sum